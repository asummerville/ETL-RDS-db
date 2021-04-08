#!/bin/python3

#steps:

##SCRIPTING

#figure out what data source i'll use. possibly a url source (multiple)

#write a script to ingest said data (include error handling)

#write another script to convert the file type of said data (include error handling)

#script to clean/transform the data. add/remove columns, etc. (include error handling)

#script that connects to a sql db and pushes the file to said db (include error handling)

#make sure to include a summary of what happend and where the file ended up

#write a "main" executable (CMD) script that takes one parameter (a url) and then just executes each of the above scripts

#README with instructions on how to use the container. tell them to run "main.py" with a url as the parameter

##DOCKER

#create a dockerfile in this folder that maps the folder and has a CMD to execute the main script