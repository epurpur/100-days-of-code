#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 15:19:22 2018

@author: ep9k
"""

import os
import csv

global_data = []

def init():
    input_field = input("Enter field name: ")       #allows me to choose input field quickly
    sliced = int(input("enter start number: "))
    gd2 = []
    ages = []
    
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'drug_use.csv')
    
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)            #this gives us an ordered dictionary, data type are strings
    
        for row in reader:
            upgrade_data_type(row)
            gd2.append(row.get(input_field))
            ages.append(row.get('age'))
    print("alcohol-use by age")
    
    return(parse_global_data(gd2, ages, sliced))
#        for row in reader:
#            upgrade_data_type(row)  
#            global_data.append((row.get('n')))      #this just appends values in 'n' column to global_data variable
#    
#    parse_global_data(global_data)     #now run parse_global_data() function



def upgrade_data_type(row):
    #this function takes the rows from the csv data and updates their data type from str to int or float
    row['n'] = int(row['n'])
    row['alcohol-use'] = float(row['alcohol-use'])
    row['marijuana-use'] = float(row['marijuana-use'])
    row['cocaine-use'] = float(row['cocaine-use'])
    row['crack-use'] = float(row['crack-use'])
    row['heroin-use'] = float(row['heroin-use'])
    row['hallucinogen-use'] = float(row['hallucinogen-use'])
    row['inhalant-use'] = float(row['inhalant-use'])
    row['pain-releiver-use'] = float(row['pain-releiver-use'])
    row['oxycontin-use'] = float(row['oxycontin-use'])
    row['tranquilizer-use'] = float(row['tranquilizer-use'])
    row['stimulant-use'] = float(row['stimulant-use'])
    row['meth-use'] = float(row['meth-use'])
    row['sedative-use'] = float(row['sedative-use'])

    return row


def parse_global_data(global_data, ages, sliced):
        print(global_data[:sliced], ages[:sliced])


