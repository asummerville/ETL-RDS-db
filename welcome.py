#!/usr/bin/python3

import os

file = input("File to ship to database: ")
os.environ['file'] = file

KAGGLE_USERNAME = input("Kaggle username: ")
os.environ['KAGGLE_USERNAME'] = KAGGLE_USERNAME

KAGGLE_KEY = input("Kaggle key: ")
os.environ['KAGGLE_KEY'] = KAGGLE_KEY

host_name = input("Server host name: ")
os.environ['host_name'] = host_name

user_name = input("MYSQL username: ")
os.environ['user_name'] = user_name

user_password = input("MYSQL password: ")
os.environ['user_password'] = user_password

db_name = input("Database name: ")
os.environ['db_name'] = db_name