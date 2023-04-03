from json import load
import uvicorn
import os
from pandas import DataFrame, read_sql_query
from networkx import from_pandas_edgelist, shortest_simple_paths, path_weight
from math import ceil
from sqlite3 import connect
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typer import Typer

#__app_name__ = "givemetheodds"
#__version__ = "0.1.0"
app_input = Typer()
app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def captureProb(k: int) -> float:
    capture_prob = sum([(9**(i-1))/(10**i) for i in range(1,k+1)])
    return capture_prob

def readConfigDB(db: str) -> DataFrame: #Add Exception/Edge Case Handles
    cnx = connect(db)
    routes_df = read_sql_query("SELECT * FROM ROUTES", cnx)
    return routes_df

def readConfigJSON(config_file: str) -> tuple: #Add Exception/Edge Case Handles
    with open(config_file) as f:
        config_dict = load(f)
        path = os.path.dirname(f.name)
    autonomy = config_dict['autonomy']
    departure = config_dict['departure']
    arrival = config_dict['arrival']
    routes_db = path + '/' + config_dict['routes_db']
    routes_df = readConfigDB(routes_db)

    return (autonomy, departure, arrival, routes_df)

def readRebelJSONSTR(rebel_file: str) -> tuple:
    with open(rebel_file) as f:
        rebel_dict = load(f)
    countdown = rebel_dict['countdown']
    bounty_hunters = rebel_dict['bounty_hunters']
    return (countdown, bounty_hunters)

def readRebelJSON(rebel_file: UploadFile) -> tuple:
    with rebel_file.file as f:
        rebel_dict = load(f)
    countdown = rebel_dict['countdown']
    bounty_hunters = rebel_dict['bounty_hunters']
    return (countdown, bounty_hunters)

def possibleRoutes(arrival, departure, countdown, autonomy, routes_df):
    #routes_df = routes_df.rename({'travel_time':'weight'}, axis='columns')
    RoutesGraph= from_pandas_edgelist(routes_df,'origin', 'destination', 'travel_time')
    valid_paths = []
    for path in shortest_simple_paths(RoutesGraph, departure, arrival, weight='travel_time'):
        path_length = path_weight(RoutesGraph, path, 'travel_time')
        fuel_time = ceil(path_length/autonomy - 1)
        if path_length + fuel_time <= countdown:
            valid_paths.append([path, path_length, fuel_time])
    return valid_paths, RoutesGraph

def routeProbs(RoutesGraph, possible_routes, autonomy, bounty_hunters):#Still Issues
    for route in possible_routes:
        #print(route)
        days = 0
        for bounty_hunter in bounty_hunters:
            #print(bounty_hunter)
            for planet in route[0]:
                if bounty_hunter['planet']==planet:
                    #Route up till matching planet
                    path = route[0][:route[0].index(planet)+1]
                    path_day = path_weight(RoutesGraph, path, 'travel_time')
                    fuel_time = 0
                    if path_day >= autonomy:
                        fuel_time = 1
                    if path_day == bounty_hunter['day'] or path_day+fuel_time == bounty_hunter['day']:
                        #print(planet, path_day, bounty_hunter['day'])
                        days += 1
        route.append((1 - captureProb(days)) * 100)
    return possible_routes

def createJSON(route_probs):
    routeDict = dict()
    routeDict['route'] = route_probs[0]
    routeDict['length'] = route_probs[1]
    routeDict['fuel_time'] = route_probs[2]
    routeDict['odds'] = route_probs[3]

    return routeDict

@app.post('/uploadfile/')
async def uploadFile(rebel_filename: UploadFile): #Min Route Probs Not Proper
    
    autonomy, departure, arrival, routes_df = readConfigJSON(os.environ['odds_config_filename'])
    if not rebel_filename:
        return {'No File Sent'}
    countdown, bounty_hunters = readRebelJSON(rebel_filename)
    possible_routes, RoutesGraph = possibleRoutes(arrival, departure, countdown, autonomy, routes_df)
    
    if possible_routes:
        route_probs = routeProbs(RoutesGraph, possible_routes, autonomy, bounty_hunters)
        return createJSON(route_probs[0])
    else:
        return {'route:':'No Way Jose', 'odds': 0}

@app_input.command()
def init_handle(init_filename: str): 
    os.environ['odds_config_filename'] = init_filename
    uvicorn.run("odds_backend:app", host="0.0.0.0", port=8000, reload=True)
    #app()

if __name__=="__main__":
    app_input()