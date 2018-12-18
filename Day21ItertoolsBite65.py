#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:52:36 2018

@author: ep9k
"""

import itertools
import os
import urllib.request
import string
import random

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])
    #dictionary object is a set of 234371 words

#Generates 7 random letters
letters = [(random.choice(string.ascii_lowercase)) for i in range(4)]
print("Letters are:", letters)


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    pass

def _get_permutations_draw_all_letters(draw = letters):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)
       Note - This works only for full length of letters draw
       Letters are generated randomly"""

    team_size = len(letters)    #team_size refers to length of pairs (a, ae, aei, etc...)
    for i in range(team_size):
        team_size = i
        permutations = list(itertools.permutations(draw, team_size))
        dict_matches = [''.join(i) for i in permutations]
        
    #make list of permutations, join them and append to result if match with dictionary word
    
    #dict_matches = [''.join(i) for i in permutations]
    result = ([i for i in dict_matches if i in dictionary])
    
    return(result)   

print(_get_permutations_draw_all_letters())