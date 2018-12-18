#This is the main module for my weather app
#I'm submitting an API request to Open Weather Map's API (https://openweathermap.org/api)


#import daily_forecast_functions as dff
#import extended_forecast_functions as eff
import sys
import csv
import requests
import json
import logbook
import time


def main():
    """Weather app main module
    daily_forecast_functions and extended_forecast_functions contain individual descriptions of what each function does"""
    
    print("~~~~~~Erich's Weather~~~~~~~~")
    print("We will check the weather at various climbing destinations by state")

    forecast_time = input("Do you want today's forecast or 5 day forecast? (Enter [1] or [5]) : ")
    if forecast_time == '1':
        user_state_choice = state_choice(input("Enter state abbreviation (in caps) : "))
    
        city_id_list = user_state_choice[0]     #list of city ids returned from state_choice
        climbing_area_alias = user_state_choice[1]  #list of climbing area aliases returned from state_choice
    
        json_data = single_dynamic_api_request(city_id_list)

        display_conditions_today(json_data, climbing_area_alias)


         
def state_choice(state):
    """Asks for user_state_choice and imports csv('ClimbingAreasCityID.csv') of climbing areas by state. Looks for state in list, then returns list 
    of city_ids and their climbing_area_alias for each location"""
    
    city_id_list = []
    climbing_area_alias = []
    
    with open('ClimbingAreasInfo.csv') as file:
        reader = csv.reader(file)
        my_list = list(reader)
    
    for i in my_list:
        if i[0] == state:
            climbing_area_alias.append(i[2])
            city_id_list.append(i[3])
    return city_id_list, climbing_area_alias        
    

def single_dynamic_api_request(city_id_list):
    """city_id_list is returned from state_choice and uses them to create api request to return weather for city."""
    
    city_id_string = ','.join([str(city) for city in city_id_list])         #String comprehension to make one string from list of strings in city_id_list ex:"763942,539671,334596". API request can take up to 20 cities at at time
    
    request = requests.get(f'http://api.openweathermap.org/data/2.5/group?APPID=333de4e909a5ffe9bfa46f0f89cad105&id={city_id_string}&units=imperial')

    json_data = json.loads(request.text)
    
#    pprint(json_data) #including this in case you want to see pprint json data for each city in list
    return json_data    


def display_conditions_today(json_data, climbing_area_alias):
    """gets json data from create_dynamic_api_request (after API request is made)
    and climbing_area_alias is list of climbing areas near towns (not necessarily town names themselves).
    Then, this function parses the JSON data returned for each location and prints it in a human readable format.
    Lastly, creates a conditions score for each location in the conditions dict (temp x humidity for each location)
    and prints the lowest conditions score for today. However, this logic is flawed because at some point it gets too cold or too hot and 
    conditions worsen again. 
    
    In the future I need to build in stops for temps that are too cold or too hot or too humid."""
    
    api_log = logbook.Logger("API Level (display_conditions_today())")
    t_begin = time.time()
    
    
    print("Today's climbing weather forecast... \n")
    
    climbing_area_alias_count = 0
    #I create this count because climbing_alias_for_city is a list of climbing areas and I need to step through them each time I print info for a city
    #EX: Birmingham is the city but Moss Rock Preserve is the climbing area. Each time I run the 'for city in data['list']' loop, I need the corresponding climbing area name for each time I loop through

    try:        #try/except block here to handle KeyError
        for city in json_data['list']:
            if city['sys']['country'] != 'US':
                print(f"City: {city['name']}, {city['sys']['country']}")
                print(f"Climbing area: {climbing_area_alias[climbing_area_alias_count]}")
                print(f"Temp today: {city['main']['temp']}")
                print(f"Humidity: {city['main']['humidity']}")
                print(f"Weather: {city['weather'][0]['description']}\n")    #need ['weather'][0]['description']. The description is item 0 in a list inside 'weather'
                climbing_area_alias_count += 1
            else:
                print(f"City: {city['name']}")
                print(f"Climbing area: {climbing_area_alias[climbing_area_alias_count]}")
                print(f"Temp today: {city['main']['temp']}")
                print(f"Humidity: {city['main']['humidity']}")
                print(f"Weather: {city['weather'][0]['description']}\n")    #need ['weather'][0]['description']. The description is item 0 in a list inside 'weather'
                climbing_area_alias_count += 1
    
        conditions_dict = {}        #Making a dict to store 'Name': 'Conditions_score' as key,value pair
     
        for city in json_data['list']:
            conditions_dict[city['name']] = (city['main']['temp']*city['main']['humidity'])
        print(f"Currently, the best conditions are in {min(conditions_dict, key=conditions_dict.get)}.")  
    
        api_log.trace("Search successful")

        t_end = time.time()
        api_log.trace(f"Finished search. Results in {(t_end-t_begin)} seconds")
    
    except KeyError:
        msg1 = ("**Key Error** Either the state you entered is not in the database...")
        msg2 = ("Or there is a problem in the with/open block in the state_choice() function")

        api_log.warn(msg1 + msg2)
    


def init_logging(filename: str = None):
    level = logbook.TRACE
#    level = logbook.WARNING
    
    if filename:        #if a filename is provided as an argument 
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()  #TimedRotatingFileHandler uses date as part of logging. Pushes this output to the log file
    else:               #if a filename is not provided
        logbook.StreamHandler(sys.stdout, level=level).push_application()       #Pushes output to stdout (in console) if no log file is specified

    msg = f"Logging Initialized. level: {level}, mode: {'stdout mode' if not filename else 'file mode: ' + filename}"    #gives mode. Either stdout (no filename) or filemode (if filename specified)

    logger = logbook.Logger('Startup')
    logger.notice(msg)

if __name__ == '__main__':
#    init_logging('ClimbingWeatherAppLogbook')
    init_logging()
    main()
