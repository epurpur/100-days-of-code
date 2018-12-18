#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 07:55:04 2018

@author: ep9k
"""
import random

class Roll:
    def __init__(self, name):
        self.name = name

    def play():
        plays = ['rock', 'paper', 'scissors']
        my_play = input("choose [r]ock, [p]aper, or [s]cissors ")
        if my_play == 'r':
            my_play = 'rock'
        elif my_play == 'p':
            my_play = 'paper'
        else:
            my_play = 'scissors'
        cpu_play = (random.choice(plays))
        
        print ("Player 1 chooses: ", my_play)
        print ("Player 2 chooses: ", cpu_play)
        
        return my_play, cpu_play
        

class Player:
    def __init__(self, name):
        self.name = name                    #we only need a name, I give it a default value of "Erich"
    
    