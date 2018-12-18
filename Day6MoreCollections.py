#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 10:40:13 2018

@author: ep9k
"""
import csv
from collections import namedtuple, defaultdict, Counter

#Working with HIV dataset from CDC (Center for Disease Control)
#we will make a defaultdict where keys are States and values are Cases, Rate per 100k, and Population
hiv_data ='hiv_data.csv'
Entity = namedtuple('State_name', 'hiv_cases hiv_rate state_pop')     #creating placeholders for key and values

def get_state_hiv_data(data=hiv_data):       #data is hiv_data.csv by default
    """Extracts states from csv and stores them in a dictionary
    where keys are directors and values are a list of movies (named tuples)"""
    states = defaultdict(list)
    with open(data) as f:
        for line in csv.DictReader(f):
            state = line['Geography']
            Cases = line['Cases']
            Rate = line['Rate100k']
            Population = line['Population']
        
            e = Entity(hiv_cases=Cases, hiv_rate=Rate, state_pop=Population)
            states[state].append(e)
    
    return states
print(get_state_hiv_data())
#states = get_state_hiv_data()
#print(type(states))
#print(states['Alabama'])
#print(states['North Carolina'])
#print(states['Virginia'])



"""
numbers = []
for k, v in states.items():    
    v = str(v)
    v = v.split(' ')
    v = v[2]
    v = v[12:]
    v = (v.split("'"))
    v = v[0]
    v = v.replace(',','')
    numbers.append(int(v))
print (numbers)

highest = 0
for number in numbers:
    if number > highest:
        highest = number
print("Highest number:", highest)
"""

