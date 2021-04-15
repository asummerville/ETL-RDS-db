#!/usr/bin/python

#convert csv to sql and push it to a db

import mysql.connector
from mysql.connector import Error
import pandas as pd
import os

#establish connection fxn
def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#execute query fxn
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as err:
        print(f"Error: '{err}'")

#env variables + other data
df = pd.read_csv('./df.csv') 
file_name = os.getenv('file_name')
host_name = os.getenv('host_name')
user_name = os.getenv('user_name')
user_password = os.getenv('user_password')
db_name = os.getenv('db_name')

connection = create_server_connection(host_name, user_name, user_password, db_name)

f = file_name.replace('.csv', '')

#create new table
table_query = f'CREATE TABLE {f} (popularity float(2), danceability float(4), energy float(4), acousticness float(4))'
execute_query(connection, table_query)

#add data from df to table
cursor = connection.cursor()
for row in list(range(0,len(df))):
    sql = f'INSERT INTO {f}(popularity, danceability, energy, acousticness) VALUES (%s,%s,%s,%s)'
    pop_val = df['popularity'].iloc[row]
    dance_val = df['danceability'].iloc[row]
    en_val = df['energy'].iloc[row]
    ac_val = df['acousticness'].iloc[row]
    cursor.execute(sql, (pop_val, dance_val, en_val, ac_val))
connection.commit()

del os.environ['user_password']
del os.environ['KAGGLE_KEY']