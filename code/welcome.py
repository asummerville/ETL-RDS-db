#!/usr/bin/python

import os
import getpass


files_list = ['data.csv', 'data_by_artist.csv', 'data_by_artist_o.csv', 'data_by_genres.csv', 'data_by_genres_o.csv', 'data_by_year.csv', 'data_by_year_o.csv', 'data_o.csv', 'data_w_genres.csv', 'data_w_genres_o.csv']

while True:
    file_name = input("File to ship to database: ")
    if file_name in files_list:
        break
    else:
        print('Enter a valid file name (ex. data.csv, data_by_genres.csv, etc.)')
os.environ['file_name'] = str(file_name)

KAGGLE_USERNAME = input("Kaggle username: ")
os.environ['KAGGLE_USERNAME'] = str(KAGGLE_USERNAME)

KAGGLE_KEY = getpass.getpass("Kaggle key: ")
os.environ['KAGGLE_KEY'] = str(KAGGLE_KEY)

host_name = input("Server host name: ")
os.environ['host_name'] = str(host_name)

user_name = input("MYSQL username: ")
os.environ['user_name'] = str(user_name)

user_password = getpass.getpass("MYSQL password: ")
os.environ['user_password'] = str(user_password)

db_name = input("Database name: ")
os.environ['db_name'] = str(db_name)