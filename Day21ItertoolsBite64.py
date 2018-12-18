#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 13:32:05 2018

@author: ep9k
"""

import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
    zipped_up = list(itertools.zip_longest(names, locations, confirmed, fillvalue = '-'))
    return(zipped_up)

print(get_attendees())


if __name__ == '__main__':
    get_attendees()