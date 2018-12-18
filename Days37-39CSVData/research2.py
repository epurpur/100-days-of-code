#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 10:58:16 2018

@author: ep9k
"""
import os
import csv
import collections


datax = []
Record = collections.namedtuple(            #arguments are a name and the arguments/fields it takes
    'Record',
    'date,actual mean temp,actual_min_temp,actual_max_temp,'
    'average_min_temp,average_max_temp,record_min_temp,record_max_temp,'
    'record_min_temp_year,record_max_temp_year,actual_precipitation,'
    'average_precipitation,record_precipitation'    
)


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'seattle_weather_data.csv')
    
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        datax.clear()
        for row in reader:
            record = parse_row(row)
            
            datax.append(record)
            #print(type(record.actual_precipitation), (record.actual_precipitation)) 
            #these are namedtuples. much easier syntax
            
def parse_row(row):
    row['actual mean temp'] = int(row['actual mean temp'])
    row['actual_min_temp'] = int(row['actual_min_temp'])
    row['actual_max_temp'] = int(row['actual_max_temp'])
    row['average_min_temp'] = int(row['average_min_temp'])
    row['average_max_temp'] = int(row['average_max_temp'])
    row['record_min_temp'] = int(row['record_min_temp'])
    row['record_max_temp'] = int(row['record_max_temp'])
    row['record_min_temp_year'] = int(row['record_min_temp_year'])
    row['record_max_temp_year'] = int(row['record_max_temp_year'])
    row['actual_precipitation'] = float(row['actual_precipitation'])
    row['average_precipitation'] = float(row['average_precipitation'])
    row['record_precipitation'] = float(row['record_precipitation'])
    
#    record = Record(**row)         #shorthand for below
    record = Record(                #gives variable name to each row in record
        date = row.get('date'),
        actual_mean_temp = row.get('actual mean temp'),
        actual_min_temp = row.get('actual_min_temp'),
        actual_max_temp = row.get('actual_max_temp'),
        average_min_temp = row.get('average_min_temp'),
        average_max_temp = row.get('average_max_temp'),
        record_min_temp = row.get('record_min_temp'),
        record_max_temp = row.get('record_max_temp'),
        record_min_temp_year = row.get('record_min_temp_year'),
        record_max_temp_year = row.get('record_max_temp_year'),
        actual_precipitation = row.get('actual_precipitation'),
        average_precipitation = row.get('average_precipitation'),
        record_precipitation = row.get('record_precipitation')
        
        )
    
    
    return record

def hot_days():
    return sorted(datax, key=lambda r: r.actual_max_temp, reverse=True)

def cold_days():
    return sorted(datax, key=lambda r: r.actual_min_temp)

def wet_days():
    return sorted(datax, key=lambda r: r.actual_precipitation, reverse=True)
      

                                  