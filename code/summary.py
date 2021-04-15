#!/usr/bin/python

import pandas as pd

#sumamry
print("Your data table has 4 columns and 500 observations")
print("The 4 columns include: popularity, danceability, energy, and acousticness")

data = pd.read_csv('./df.csv') 
df = pd.DataFrame(data)

df = df.drop('Unnamed: 0', axis=1)

max_pop = max(df['popularity'])
max_dance = max(df['danceability'])
max_en = max(df['energy'])
max_a = max(df['acousticness'])

print(f"The maximum popularity is {max_pop}, danceabliity {max_dance}, energy {max_en}, acousticness {max_a}")

print("You may view your table in whatever database you pushed it to")
print("Goodbye!")