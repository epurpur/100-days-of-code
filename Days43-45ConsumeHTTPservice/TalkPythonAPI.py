#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:11:22 2018

@author: ep9k
"""
import requests
import collections

Movie = collections.namedtuple('Movie', 'imdb_code, title, director, keywords, '
                               'duration, genres, rating, year, imdb_score')


def find_movie_by_title(keyword):
    
    url = f'http://movie_service.talkpython.fm/api/search/{keyword}'
    
    response = requests.get(url)
    
    response.raise_for_status()     #if things went wrong for any reason this will raise an error
    
    results = response.json()       #converts json response to dictionary
    
    movies = []
    for r in results.get('hits'):
        movies.append(Movie(**r))
        
    return movies


