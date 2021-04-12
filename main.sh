#!/bin/bash

set -e

#create env variable with the url parameter the user inputs

# $1 will be the dataset file name
#find better way to ask for inputs...
export file=$1
export KAGGLE_USERNAME=$2
export KAGGLE_KEY=$3
export host_name=$4
export user_name=$5
export user_password=$6
export db_name=$7

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

