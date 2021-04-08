#!/bin/bash

set -e

#create env variable with the url parameter the user inputs

# $1 will be the dataset file name
export file=$1
export KAGGLE_USERNAME=$2
export KAGGLE_KEY=$3

# # #run each ETL py script:

#grab the data using the kaggle API
echo "Attempting fetch..."
ingest_script="./ingest.py"
$ingest_script
sleep 2
echo "Fetch complete"

# #convert the file type to SQL
# echo "Converting file..."
# convert_script="./convert.py"
# $convert_script
# sleep 2
# echo "Conversion complete"

# #transform file
# echo "Transforming file..."
# transform_script="./transform.py"
# $transform_script
# sleep 2
# echo "Transformation complete"

# #push to RDS
# echo "Pushing to RDS database..."
# rds_script="./rds-push.py"
# $rds_script
# sleep 2
# echo "Push complete"

# #summary
# echo "Process completed!"
# summary_script="./summary.py"
# $summary_script

