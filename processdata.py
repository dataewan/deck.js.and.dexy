#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import os

import json

FILTERGENRE = "Thriller"
output = {}
output['genre'] = FILTERGENRE

datadir = "/home/ewan/Datasets/grouplens/ml-100k/"

datafilename = os.path.join(datadir, "u.data")
itemfilename = os.path.join(datadir, "u.item")
userfilename = os.path.join(datadir, "u.user")

data = pd.read_table(datafilename,
                    sep="\t",
                    names = ["uid", "iid", "rating", "timestamp"],
                    header=None)

items = pd.read_table(itemfilename,
                     sep="|",
                     names = ["iid", "title", "releasedate", "videoreleasedate",
                             "imdburl", "unknown", "Action", "Adventure",
                              "Animation", "Children's", "Comedy", "Crime",
                              "Documentary", "Drama", "Fantasy", "Film-Noir",
                              "Horror", "Musical", "Mystery", "Romance",
                              "Sci-Fi", "Thriller", "War", "Western"],
                      encoding = 'latin1',
                      header = None)

users = pd.read_table(userfilename,
                     sep = "|",
                     names = ["uid", "age", "gender", "occupation", "zipcode"],
                     header = None)

merged = data.merge(items)
merged = merged.merge(users)

if FILTERGENRE is not None:
    ratings = merged[merged[FILTERGENRE] == 1]
else:
    ratings = merged

output['number'] = len(ratings)

# calculate the 10 highest rated movies in this group.
movieratings = ratings.pivot_table('rating',
                    rows = 'title')
movieratings = pd.DataFrame(movieratings).sort("rating", ascending=False)

output['top10'] = movieratings[:10].to_html()
# also calculate the worst film
output['worstfilm'] = movieratings[-1:].to_html()

# figure out the films that polarise males and females.
gender_ratings = ratings.pivot_table('rating',
                                     rows='title',
                                     cols = 'gender')

gender_ratings.columns = ["Female rating", "Male rating"]
gender_ratings['Difference'] = gender_ratings['Female rating'] - gender_ratings['Male rating']
gender_ratings =  gender_ratings.dropna().sort("Difference", ascending = False)
output['top_female_films'] = gender_ratings[:5].to_html()

gender_ratings['Difference'] = gender_ratings['Male rating'] - gender_ratings['Female rating']
gender_ratings =  gender_ratings.sort("Difference", ascending = False)
output['top_male_films'] = gender_ratings.dropna()[:5].to_html()

print json.dumps(output)
