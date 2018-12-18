
import logbook
import sys
import json
import requests
from pprint import pprint
import time

###################################

#request is for Boone and Charlottesville. Boone id = 4456703, Charlottesville id = 4752031
city_id = '3120968'

app_log = logbook.Logger('App Level')


def make_api_request(city_id):
    try:
        api_log = logbook.Logger("API Level")
        
        t0 = time.time()
        api_log.trace(f'Starting search for city_id: {city_id}')
        
        r = requests.get(f'http://api.openweathermap.org/data/2.5/group?APPID=333de4e909a5ffe9bfa46f0f89cad105&id={city_id}&units=imperial')
        
        data = json.loads(r.text)
        
        api_log.trace(f"Request finished, status code {r.status_code}")
        
        #names = data['list']
        for city in data['list']:
            if city['sys']['country'] != 'US':
                print(f"City: {city['name']}, {city['sys']['country']}")
                print(f"Temp today: {city['main']['temp']}")
                print(f"Humidity: {city['main']['humidity']}\n")
            else:
                print(f"City: {city['name']}")
                print(f"Temp today: {city['main']['temp']}")
                print(f"Humidity: {city['main']['humidity']}\n")
                
        api_log.trace(f'Search successful for city_id: {city_id}' )
        
        t1 = time.time()
        api_log.trace(f'Finished search for city_id: {city_id}. Results in {int((t1-t0)*1000)} milliseconds')
        
        
    except KeyError:
        msg = 'Error! Something is wrong with the api request. Maybe a city_id is wrong or your API key is bad'
        api_log.warn(msg)
            
            
def init_logging(filename: str = None):
    level = logbook.TRACE            #hierarchy of levels in logging include trace, error, notices, etc. I'm using TRACE so that it is verbose in what it reports.
    
    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application() #TimedRotatingFileHandler uses date as part of logging. Pushes this output to the log file
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()   #Pushes output to stdout (in console) if no log file is specified
        
    msg = f"Logging Initialized. level: {level}, mode: {'stdout mode' if not filename else 'file mode: ' + filename}"
    
    logger = logbook.Logger('Startup')
    logger.notice(msg)
            
    
init_logging()      #writes this to a log file specified as the argument + the date_format from TimedRotatingFileHandler IF a filename is given
make_api_request(city_id)