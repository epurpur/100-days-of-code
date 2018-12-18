#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:54:23 2018

@author: ep9k
"""

import random

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

#write list conprehension to conver these to title case (brad pitt -> Brad Pitt)
#old way with for loop
#for name in NAMES:
    #print(name.title())
#new way with list comprehension
#print([name.title() for name in NAMES])

#list comprehension to reverse name order in list
def reverse_first_last_names(name):
    first, last = name.split()
    #' '.join([last,first]) -- wait we have f-strings now
    return (f'{last} {first}')

#print([reverse_first_last_names(name) for name in NAMES])
for name in NAMES:
    name = name.title()
    first, last = name.split()
    #print(last, first)

#can also use list comprehension with functions
[reverse_first_last_names(name) for name in NAMES]

#Then use this same list and make a little generator, for example to randomly return a pair of names
def gen_pairs():
    # again a list comprehension is great here to get the first names
    # and title case them in just 1 line of code (this comment took 2)
    first_names = [name.split()[0].title() for name in NAMES]
    while True:
        
        # added this when I saw Julian teaming up with Julian (always test your code!)
        first, second = None, None
        first, second = random.sample(first_names, 2)
        
        yield f'{first} teams up with {second}'

    
pairs = gen_pairs()
#for i in range(10):
#    print(next(pairs))
#print(next(pairs))

bites = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods',
         12: 'Write a user validation function',
         13: 'Convert dict in namedtuple/json',
         14: 'Generate a table of n sequences',
         15: 'Enumerate 2 sequences',
         16: 'Special PyBites date generator',
         17: 'Form teams from a group of friends',
         18: 'Find the most common word',
         19: 'Write a simple property',
         20: 'Write a context manager',
         21: 'Query a nested data structure'}
exclude_bites = {6, 10, 16, 18, 21}


#def filter_bites(bites=bites, bites_done=exclude_bites):
#    """return the bites dict with the exclude_bites filtered out"""
#    return [x: d[x] for x in bites if x not in bites_done]


#def filtered_bites(d, keys):
def filtered_bites(bites=bites, exclude_bites=exclude_bites):
    return {k:v for k,v in bites.items() if k not in exclude_bites}
#print(filtered_bites())

