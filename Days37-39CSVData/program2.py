#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 10:58:02 2018

@author: ep9k
"""

import research2

def main():
    print()
    print("Weather research for Seattle, 2014-2015")
    print()
    research2.init()
    
    print("The hottest 5 days:")
    #going to give us all the days hottest to coldest
    days = research2.hot_days()
    for idx,d in enumerate(days[:5]):
        print("{}. {}F on {}".format(idx+1, d.actual_max_temp, d.date))
    print()
    
    print("The coldest 5 days:")
    days = research2.cold_days()
    for idx, d in enumerate(days[:5]):
        print("{}. {}F on {}".format(idx+1, d.actual_min_temp, d.date))
    print()
    
    print("The wettest 5 days:")
    days = research2.wet_days()
    for idx, d in enumerate(days[:5]):
        print("{}. {} inches of rain on {}".format(idx+1, d.actual_precipitation, d.date))


if __name__ == '__main__':
    main()