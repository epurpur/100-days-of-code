#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:10:31 2018

@author: ep9k
"""

# API key = 333de4e909a5ffe9bfa46f0f89cad105
#  &APPID=333de4e909a5ffe9bfa46f0f89cad105
# http://api.openweathermap.org/data/2.5/weather?APPID=333de4e909a5ffe9bfa46f0f89cad105&q=London,uk example of valid api call for ONE CITY
# http://api.openweathermap.org/data/2.5/group?APPID=333de4e909a5ffe9bfa46f0f89cad105&id=524901,703448&units=imperial   example of valid api call for multiple cities


#recommended I call API by city ID to get unambiguous result for my city

import json
import requests
from pprint import pprint

####################################

#request is for Boone and Charlottesville. Boone id = 4456703, Charlottesville id = 4752031
#r = requests.get('http://api.openweathermap.org/data/2.5/group?APPID=333de4e909a5ffe9bfa46f0f89cad105&id=4456703,5128539,292968,4805686,3010315,4752031,7262635,5414872,4853799,5370006,2988507,360630,1273294,7871396,6180144&units=imperial')
#
#data = json.loads(r.text)
#
##names = data['list']
#for city in data['list']:
#    if city['sys']['country'] != 'US':
#        print(f"City: {city['name']}, {city['sys']['country']}")
#        print(f"Temp today: {city['main']['temp']}")
#        print(f"Humidity: {city['main']['humidity']}\n")
#    else:
#        print(f"City: {city['name']}")
#        print(f"Temp today: {city['main']['temp']}")
#        print(f"Humidity: {city['main']['humidity']}\n")
#        
####################################

with open('city.list.json') as f:
    data = json.load(f, encoding='utf-8')
    
    city = input("Enter a city: ")
    for place in data:
        if place['name'] == city:
            print(place['id'])


def get_city_id(input_data):
    #code will be something like...
#    if city in city_list:
#        return city_id
    pass

#get_city_id()