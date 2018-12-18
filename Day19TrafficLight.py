#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 09:41:19 2018

@author: ep9k
"""

"""The idea is to cycle (hint) through different colors of a set of traffic lights (red, amber, green) printing 
    the name of the color every time the cycle occurs.
    For bonus points: traffic lights normally cycle between green and red based on traffic levels so you never
    know exactly when that will happen. This is a chance to throw some randomness into your script."""

import itertools
import time
import sys
import random

colors = 'green yellow red'.split()
colors2 = ['green', 'yellow', 'red']        #cycle also iterates through list
traffic_light = itertools.cycle(colors2)
max_width = max(map(len, colors2))

while True:
    sys.stdout.write('\r' + next(traffic_light).ljust(max_width))
    sys.stdout.flush()
    time.sleep(random.uniform(.1, 3.0))     #random.uniform(a, b) takes floats as arguments
    
#####Julian's traffic light app###
colors = 'red green yellow'.split()
rotation = itertools.cycle(colors)

def rg_timer():
    return random.randint(3, 7)

def light_rotation(rotation):
    for color in rotation:
        if color == 'yellow':
            print('Caution! the light is %s' % color)
            itertools.sleep(3)
        elif color == 'red':
            print('STOP! The light is %s' % color)
            itertools.sleep(rg_timer())
        else:
            print('Go! The light is %s' % color)
            itertools.sleep(rg_timer())


if __name__ == '__main__':
    light_rotation(rotation)