from json import load
from pandas import DataFrame, read_sql_query
from networkx import from_pandas_edgelist, shortest_simple_paths, path_weight
from math import ceil
from sqlite3 import connect
from fastapi import FastAPI

#__app_name__ = "givemetheodds"
#__version__ = "0.1.0"

app = FastAPI()

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
    autonomy = config_dict['autonomy']
    departure = config_dict['departure']
    arrival = config_dict['arrival']
    routes_db = config_dict['routes_db']
    routes_df = readConfigDB(routes_db)

    return (autonomy, departure, arrival, routes_df)

def readRebelJSON(rebel_file: str) -> tuple:
    with open(rebel_file) as f:
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

@app.get('/{init_filename}/{rebel_filename}')
async def main(init_filename:str, rebel_filename:str):
    autonomy, departure, arrival, routes_df = readConfigJSON(init_filename)
    countdown, bounty_hunters = readRebelJSON(rebel_filename)
    possible_routes, RoutesGraph = possibleRoutes(arrival, departure, countdown, autonomy, routes_df)
    
    if possible_routes:
        route_probs = routeProbs(RoutesGraph, possible_routes, autonomy, bounty_hunters)
        return {'route':route_probs}
    else:
        return {'route:':'No Way Jose'}

    #print(min(route_probs))


if __name__=="__main__":
    app()

#{"autonomy": 6,"departure": "Tatooine","arrival": "Endor","routes_db": "universe.db"}
#{"countdown": 7, "bounty_hunters": [{"planet": "Hoth", "day": 6 }, {"planet": "Hoth", "day": 7 },{"planet": "Hoth", "day": 8 }]}