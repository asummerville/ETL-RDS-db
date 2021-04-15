#!/usr/bin/python

#transform file

import pandas as pd
import numpy as np
import os

file_name = os.getenv('file_name')

#data = pd.read_csv('df.csv') 

data = pd.read_csv(f'./{file_name}') 
df = pd.DataFrame(data)

df = df[['popularity', 'danceability', 'energy', 'acousticness']]

df = df.head(500)

df = df.sort_values('popularity', ascending=False)

#df.head()

#write to csv
df.to_csv('./df.csv')
