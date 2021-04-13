#!/usr/bin/python3

import os
import getpass

file_name = input("File to ship to database: ")
os.environ['file_name'] = str(file_name)

KAGGLE_USERNAME = input("Kaggle username: ")
os.environ['KAGGLE_USERNAME'] = str(KAGGLE_USERNAME)

KAGGLE_KEY = input("Kaggle key: ")
os.environ['KAGGLE_KEY'] = str(KAGGLE_KEY)

host_name = input("Server host name: ")
os.environ['host_name'] = str(host_name)

user_name = input("MYSQL username: ")
os.environ['user_name'] = str(user_name)

user_password = getpass.getpass("MYSQL password: ")
os.environ['user_password'] = str(user_password)

db_name = input("Database name: ")
os.environ['db_name'] = str(db_name)