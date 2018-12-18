#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:02:16 2018

@author: ep9k
"""

import itertools

friends_list_boone = 'erich tilley josh leif matt dylan'.split()
friends_list_cville = 'jeff andrew taylor jake melissa cailey'.split()

def friends_team(list_of_friends, team_size=2, order_does_matter=False):
    """inputs are a friends list
    a team_size(type int, default = 2)
    order_does_matter(type bool, default False) If order does matter, more team results
    """
    if order_does_matter == False:
        print("Combinations")
        combos = (list(itertools.combinations(list_of_friends, team_size)))
        return combos, len(combos)
    else:
        print("Permutations")
        permutations = (list(itertools.permutations(list_of_friends, team_size)))
        return permutations, len(permutations)
    
    
print(friends_team(friends_list_cville))
    
    
    
