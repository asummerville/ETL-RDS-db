#!/bin/bash

set -e


#welcome message and ask for inputs:
echo "Starting..."
welcome_script="./code/welcome.py"
$welcome_script
sleep 2
echo "Let's get started:"

# # #run each ETL py script:

#grab the data using the kaggle API
echo "Attempting fetch..."
ingest_script="./code/ingest.py"
$ingest_script
sleep 2
echo "Fetch complete"

#transform file
echo "Transforming file..."
transform_script="./code/transform.py"
$transform_script
sleep 2
echo "Transformation complete"

#add data to sql table and push to a db
echo "Sending to database..."
sql_script="./code/sql.py"
$sql_script
sleep 2
echo "Your table has been shipped to a database!"

# #summary - length of data, cols left over, maybe even summary stats?
# echo "Process completed!"
# summary_script="./summary.py"
# $summary_script


#old method (for local testing)
# export file_name=$1
# export KAGGLE_USERNAME=$2
# export KAGGLE_KEY=$3
# export host_name=$4
# export user_name=$5
# export user_password=$6
# export db_name=$7

# unset file_name
# unset KAGGLE_USERNAME
# unset KAGGLE_KEY
# unset host_name
# unset user_name
# unset user_password
# unset db_name