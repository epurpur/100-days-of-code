#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 16:28:33 2018

@author: ep9k
"""

numlist = [1,2,3,4,5]

numlist.reverse()


numlist.sort()


#for num in numlist:
    #print (str(num))
    
mystring = 'julian'
#print (list(mystring))
l = list(mystring)

l.insert(5, 'n')
l[0] = "b"
del l[0]

l.insert(0, 'm')

l.pop(0)

l.append('s')

#print (l)


pybites = {'julian': 30, 'bob': 33, 'mike': 33}
#print (pybites)

people = {}
people['julian'] = 30       #creating an entry with key=julian and value=30
people['bob'] = 103

#print (people)


print (pybites.keys())      #view keys in pybites
print (pybites.items())     #key, value pairs in pybites

for keys, values in pybites.items():
    #print(keys + str(values))
    print('%s is %d years of age' % (keys, values))     #string formatting

