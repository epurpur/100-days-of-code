#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:59:25 2018

@author: ep9k
"""

import collections

User = collections.namedtuple('User', 'name age fav_hobby iq race')

user1 = User(name='Erich', age=31, fav_hobby='climbing', iq=500, race='White')

print(user1.fav_hobby)
    

