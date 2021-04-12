#!/usr/bin/python3

#convert csv to sql and push it to a db

import mysql.connector
from mysql.connector import Error
import pandas as pd

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

host_name = 'test-db.c5rxb5jruwlq.us-east-2.rds.amazonaws.com'
user_name = 'ads3pu'

db_name = 'ds3002'

create_server_connection(host_name, user_name, user_password, db_name)

f = file.replace('.csv', '')

table_query = f'CREATE TABLE {f} (artists nvarchar(50), popularity int, danceability int, energy int)'

execute_query(connection, table_query)

cursor = connection.cursor()
for row in df.itertuples():
    cursor.execute(f'''
                INSERT INTO {db_name}.dbo.{f} (artists, popularity, danceability, energy)
                VALUES (?,?,?,?)
                ''',
                row.artists, 
                row.popularity,
                row.danceability, 
                row.energy
                )
connection.commit()