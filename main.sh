#!/bin/bash

set -e

#create env variable with the url parameter the user inputs
export INPUT=$1

test="./ingest.py"
$test


# #run each ETL py script:

# #grab the data using the kaggle API
# echo "Attempting fetch..."
# ingest_script="./ingest.py"
# $ingest_script
# sleep 5

# #convert the file type to SQL
# echo "Converting file..."
# convert_script="./convert.py"
# $convert_script
# sleep 5

# #transform file
# echo "Transforming file..."
# transform_script="./transform.py"
# $transform_script
# sleep 5

# #push to RDS
# echo "Pushing to RDS database..."
# rds_script="./rds-push.py"
# $rds_script
# sleep 5

# #summary
# echo "Process completed!"
# summary_script="./summary.py"
# $summary_script

