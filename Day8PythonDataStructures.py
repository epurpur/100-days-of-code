#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 07:21:23 2018

@author: ep9k
"""

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}



def get_all_jeeps(jeeps):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    print(cars['Jeep'])
jeeps = get_all_jeeps(cars)

def get_first_model_each_manufacturer(firstmodel):
    """return a list of matching models (original ordering)"""
    for keys, values in cars.items():
        print(keys, values[0])
firstmodel = get_first_model_each_manufacturer(cars)
        
def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    valuelists = []
    trail_cars = []
    for value in cars.values():
        valuelists.append(value)
    for value in valuelists:
        for car in value:
            if 'trail' in car.lower():
                trail_cars.append(car)
    return (sorted(trail_cars))
print(get_all_matching_models())

def sort_car_models():
    """sort the car models (values) alphabetically and return the resulting cars dict"""
    valuelists = []
    trail_cars = []
    for value in cars.values():
        valuelists.append(value)
    for value in valuelists:
        for car in value:
            trail_cars.append(car)
    return (sorted(trail_cars))
print(sort_car_models())


