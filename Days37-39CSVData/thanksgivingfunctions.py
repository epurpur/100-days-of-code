#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:09:59 2018

@author: ep9k
"""

import os
import csv
import collections

data = []



def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'thanksgiving2015.csv')
    
    with open(filename, 'r', encoding = 'utf-8') as f:
        reader = csv.DictReader(f)
        
        data.clear()
        
        for row in reader:
            print(row.get('main_dish'))
            
        

            
        





        
            
        

        
def shorter_column_names(row):
    
    pass


         
        
        

        
    

