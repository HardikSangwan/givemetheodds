from typer import Typer
from odds_backend import readConfigJSON, readRebelJSONSTR, possibleRoutes, routeProbs

app = Typer()

@app.command()
def input_handle(init_filename:str, rebel_filename:str):
    autonomy, departure, arrival, routes_df = readConfigJSON(init_filename)
    countdown, bounty_hunters = readRebelJSONSTR(rebel_filename)
    possible_routes, RoutesGraph = possibleRoutes(arrival, departure, countdown, autonomy, routes_df)
    
    if possible_routes:
        route_probs = routeProbs(RoutesGraph, possible_routes, autonomy, bounty_hunters)
        print(route_probs[0][3]) #Need best odds values
    else:
        print(0)
        #print('No Way Jose')


if __name__=="__main__":
    app()