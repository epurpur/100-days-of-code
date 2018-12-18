#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 19:43:52 2018

@author: ep9k
"""

import csv
from collections import namedtuple, defaultdict, Counter
#import urllib.request

#we will make a defaultdict where keys are directors and values are movies they have directed
#movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'
#urllib.request.urlretrieve(movie_data, movies_csv)

#defined a namedtuple called movie with title, year, score as values

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data=movies_csv):        #data is movies.csv by default
    """Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)                   #initialize a defaultdict of lists called directors
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):              #csv.dictreader parses every line into an ordered dict
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '') #replaces nonsense on end of string
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:                      #ignores incomplete data (if ValueError comes up)
                continue

            m = Movie(title=movie, year=year, score=score)  #initializes Movie namedtuple and gives it movie year and score
            directors[director].append(m)           #namedtuple gets appended to the director in the directors name list

    return directors

directors = get_movies_by_director()
print (directors['Peter Jackson'])

#user counter to find the directors with the most movies
"""
cnt = Counter()
for director, movies in directors.items():
    cnt[director] += len(movies)

print (cnt.most_common(5))
"""



                
                
                


