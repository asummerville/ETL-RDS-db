#!/usr/bin/python3

#transform file

import pandas as pd
import os

file = str(os.getenv('file'))

data = pd.read_csv(f'./{file}') 
df = pd.DataFrame(data)

df = df[['artists', 'popularity', 'danceability', 'energy']]

df = df.sort_values('popularity', ascending=False)

df.head()