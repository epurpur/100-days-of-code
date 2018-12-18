#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 10:07:10 2018

@author: ep9k
"""

import TalkPythonToMeAPI as api

def main():
    keyword = input("Enter keyword to search for : ")
    results = api.find_podcast_with_keyword(keyword)
    
    print(f"Searching with keyword: {keyword} returned {len(results)} results\n")

    
    for r in results:   #r is a dictionary for each result returned from keyword search
#        print(f"Episode Title: {r.get('title')}")
#        print(f"Episode Description: {r.get('description')}\n")
        print("Episode Title: {r.title}")
        print("Episode Description: {r.description}")

        

if __name__ == '__main__':
    main()
    
    
    ########Fix namedtuples