#!/bin/bash

set -e

#welcome message and ask for inputs:
echo "Starting..."
welcome_script="./welcome.py"
$welcome_script
sleep 2
echo "Let's get started:"

# # #run each ETL py script:

#grab the data using the kaggle API
echo "Attempting fetch..."
ingest_script="./ingest.py"
$ingest_script
sleep 2
echo "Fetch complete"

#transform file
echo "Transforming file..."
transform_script="./transform.py"
$transform_script
sleep 2
echo "Transformation complete"

#add data to sql table and push to a db
echo "Sending to database..."
sql_script="./sql.py"
$sql_script
sleep 2
echo "Your table has been shipped to a database!"

# #summary - length of data, cols left over, maybe even summary stats?
# echo "Process completed!"
# summary_script="./summary.py"
# $summary_script

