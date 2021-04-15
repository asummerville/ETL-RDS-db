#!/usr/bin/python

#welcome message and ask for inputs:
print("Starting...")
import welcome
print("Let's get started:")

# # #run each ETL py script:

#grab the data using the kaggle API
print("Attempting fetch...")
import ingest
print("Fetch complete")

#transform file
print("Transforming file...")
import transform
print("Transformation complete")

#add data to sql table and push to a db
print("Sending to database (may take a few seconds)...")
import sql
print("Your table has been shipped to a database!")

#summary of data table
import summary