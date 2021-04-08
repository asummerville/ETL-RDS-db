# DS 3002 - Data Science Systems

## Data Project 1

### ETL Prompt

You should write this as a container that can be run and tested locally. Your application should be prepared to fetch and process data based on a parameter fed into it at runtime. This can be by URL, or ID, or filename, etc. (Your choice.) The file may also be local to the container or remote via URL. (Again, your choice.) If you want to stage data in an S3 bucket for testing and grading, that's fine! Be sure to deliver all the required benchmarks.

For example: You find a series of open-source data files published to the web, and your container requires a URL for each file fed into it. From there your app fetches the file, processes and transforms it, and then returns an output file along with summary data, etc. Your application can return the file locally to the user or push it to S3, etc. afterward. The user should be given the location of the output file.
