#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:56:48 2018

@author: ep9k
"""
import json
import csv
from pprint import pprint
import requests
import logging_functions

def get_city_id():
    """parses json file (filename - city.list.json) of all places and returns city_id for place entered by user.
    Not really for use in program, I use this on the side to quickly search json file (in folder with other data)
    However, it is kind of difficult to use because many cities do not have unique names. Result is usually a long list
    of city ids which are unintelligible by themselves"""
    with open('city.list.json') as file:
        data = json.load(file, encoding='utf-8')
    
        city = input("Enter a city: ")
        for place in data:
            if place['name'] == city:
                print(place['id'])
         

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
    

#@logging_functions.my_logger
def single_dynamic_api_request(city_id_list):
    """city_id_list is returned from state_choice and uses them to create api request to return weather for city."""
    
    city_id_string = ','.join([str(city) for city in city_id_list])         #String comprehension to make one string from list of strings in city_id_list ex:"763942,539671,334596". API request can take up to 20 cities at at time
    
    request = requests.get(f'http://api.openweathermap.org/data/2.5/group?APPID=333de4e909a5ffe9bfa46f0f89cad105&id={city_id_string}&units=imperial')

    json_data = json.loads(request.text)
    
#    pprint(json_data) #including this in case you want to see pprint json data for each city in list
    return json_data    

@logging_functions.my_logger
def display_conditions_today(json_data, climbing_area_alias):
    """gets json data from create_dynamic_api_request (after API request is made)
    and climbing_area_alias is list of climbing areas near towns (not necessarily town names themselves).
    Then, this function parses the JSON data returned for each location and prints it in a human readable format.
    Lastly, creates a conditions score for each location in the conditions dict (temp x humidity for each location)
    and prints the lowest conditions score for today. However, this logic is flawed because at some point it gets too cold or too hot and 
    conditions worsen again. 
    
    In the future I need to build in stops for temps that are too cold or too hot."""
    
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
    
    except KeyError:
        print("**Key Error** Either the state you entered is not in the database...")
        print("Or there is a problem in the with/open block in the state_choice() function")
