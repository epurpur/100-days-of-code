#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 13:58:12 2018

@author: ep9k
"""
from pprint import pprint
import requests
import json

def create_dynamic_api_request():
    """city_id_list is sent from state_choice and adds them into api request to return weather for city."""
    
    r = requests.get(f'http://api.openweathermap.org/data/2.5/group?APPID=333de4e909a5ffe9bfa46f0f89cad105&id=2127202&units=imperial')

    data = json.loads(r.text)
    pprint(data)
    
create_dynamic_api_request()