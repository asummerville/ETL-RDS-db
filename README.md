# DS 3002 - Data Science Systems

## Data Project 1 - ETL

## Overview

The purpose of this project is to extract, transform, and send files from a kaggle spotify dataset to a MySQL database.

## Usage

To use the program, run this docker container `docker run -it ads3pu/dataproject:latest` and the program will automatically start

## Inputs

You'll be asked for a series of inputs: 

 - **file_name** : one of the file names (data.csv, data_by_artist.csv, etc.) from [this](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=data.csv) kaggle dataset about spotify tracks from 1921-2020.
 - **KAGGLE_USERNAME** : your kaggle username (create an account if necessary)
 - **KAGGLE_KEY** : your kaggle api key. If you don't have a key yet, go to the 'account' tab in your settings and 'create new API token' (will be deleted from env after program runs)
 - **host_name** : the server (endpoint) name of your database
 - **user_name** : your MySQL username
 - **user_password** : your MySQL password (will be deleted from env after program runs)
 - **db_name** : the database you want the file to be pushed to
