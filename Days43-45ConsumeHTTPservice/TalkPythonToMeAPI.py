#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 10:07:11 2018

@author: ep9k
"""

import requests
import collections

Episode = collections.namedtuple('Episode', 'id, url, title, description, category')    #id, url, etc are keys returned in results dictionary

def find_podcast_with_keyword(keyword):
    
    url = f'http://search.talkpython.fm/api/search?q={keyword}'
    
    response = requests.get(url)
    response.raise_for_status()
    results = response.json()   #converts response into python dictionaries called results
    
#    return results.get('results')   #'results' is the key in the dictionary that has the info about the podcast episodes
    episodes = []
    
    for r in results.get('results'):
        episodes.append(Episode(**r))       #**r preserves dictionary information for each element in dictionary. much like **args in decorators
    
#find_podcast_with_keyword('mongodb')
    



######Fix namedtuples