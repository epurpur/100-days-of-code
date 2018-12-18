#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:04:01 2018

@author: ep9k
"""
import re

string = 'I have not written in the diary in 2 weeks now.'

with open("Training2018.txt",'r', encoding='utf-8') as text:
    match_list = []
    
    data = text.read()
    match1 = (re.findall(r'\d+/\d+', data))        #\d+ is the key here. This matches 1 or more digits. matches dd/mm format dates
    match2 = (re.findall(r'\d+/\d+/\d+', data))     #matches dd/mm/yyyy format dates
    match_list.append(match1)
    match_list.append(match2)
    print(len(match_list[0] + match_list[1]))       #prints length of total number of items in match_list
    
#print(re.search(r'written', string))
