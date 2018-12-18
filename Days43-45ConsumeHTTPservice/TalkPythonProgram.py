#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 20:11:18 2018

@author: ep9k
"""

"""Using movie_service.talkpython.fm as a MovieDB service.
This is a RESTful movie service which delivers JSON data
for various movies in the database. You can query it and get 
back JSON."""

import TalkPythonAPI as api

def main():
    keyword = input("Enter keyword for title search: ")
    results = api.find_movie_by_title(keyword)
    
    for result in results:
        print(f"{result.title} has score {result.imdb_score}")


if __name__ == '__main__':
    main()