#!/usr/bin/python3

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
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

#execute query fxn
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as err:
        print(f"Error: '{err}'")


# host_name = 'test-db.c5rxb5jruwlq.us-east-2.rds.amazonaws.com'
# user_name = 'ads3pu'
# user_password = 'lebron10'
# db_name = 'ds3002'

#env variables + other data
df = pd.read_csv('./df.csv') 
file = str(os.getenv('file'))
host_name = str(os.getenv('host_name'))
user_name = str(os.getenv('user_name'))
user_password = str(os.getenv('user_password'))
db_name = str(os.getenv('db_name'))

connection = create_server_connection(host_name, user_name, user_password, db_name)

f = file.replace('.csv', '')

#create new table
table_query = f'CREATE TABLE {f} (artists nvarchar(50), popularity int, danceability float(4), energy float(4))'
execute_query(connection, table_query)

#add data from df to table
cursor = connection.cursor()
for row in list(range(0,len(df))):
    sql = f'INSERT INTO {f}(artists, popularity, danceability, energy) VALUES (%s,%s,%s,%s)'
    art_val = df['artists'].iloc[row]
    pop_val = df['popularity'].iloc[row]
    dance_val = df['danceability'].iloc[row]
    en_val = df['energy'].iloc[row]
    cursor.execute(sql, (art_val, pop_val, dance_val, en_val))
connection.commit()

