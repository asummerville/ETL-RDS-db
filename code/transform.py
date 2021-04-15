#!/usr/bin/python

#transform file

import pandas as pd
import os

file_name = os.getenv('file_name')

data = pd.read_csv(f'./{file_name}') 
df = pd.DataFrame(data)

df = df[['popularity', 'danceability', 'energy', 'acousticness']]

#df = df.astype({'popularity': 'int32', 'danceability': 'int32', 'energy': 'int32', 'acousticness': 'int32'})

df = df.astype(str)

#df.dtypes

df = df.sort_values('popularity', ascending=False)

df = df.head(500)

#df.head()

#write to csv
df.to_csv('./df.csv')
