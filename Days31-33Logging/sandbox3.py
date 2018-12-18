import json
import requests


def my_logger(original_function, filename = "logfileFF.log"):  ###THIS IS WHERE I'M STRUGGLING
    import logbook
    import sys
    level = logbook.TRACE

    if filename:
        logbook.TimedRotatingFileHandler(filename, level=level).push_application()
    else:
        logbook.StreamHandler(sys.stdout, level=level).push_application()

    msg = f"Logging Initialized. level: {level}, mode: {'stdout mode' if not filename else 'file mode: ' + filename}"
    logger = logbook.Logger("Startup level")
    logger.notice(msg)
    logger.trace(f"Starting request for city id: {city_id}")

    def wrapper(*args, **kwargs):

        result = original_function(*args, **kwargs)    
        
        wrap_logger = logbook.Logger("Wrapper Level")
        wrap_logger.trace(f"Search finished for city id: {city_id}")
        
        return result

    return wrapper


def my_timer():
    pass





city_id = '3120968'

@my_logger
def make_api_request(city_id):
    try:        
        r = requests.get(f'http://api.openweathermap.org/data/2.5/group?APPID=333de4e909a5ffe9bfa46f0f89cad105&id={city_id}&units=imperial')
        
        data = json.loads(r.text)
        
        
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
        
        
    except KeyError:
        msg = 'Error! Something is wrong with the api request. Maybe a city_id is wrong or your API key is bad'
        print(msg)
     

make_api_request(city_id)