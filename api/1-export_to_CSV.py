#!/usr/bin/python3
# This line specifies the shebang line, indicating that this script should be run with Python 3.

"""
    A script that gathers data in an API
    and displays information about a 
    specific employee's task
"""
# This is a multiline string (docstring) that provides a brief description of what the script does.

# import the necessary modules
from sys import argv
import csv
import json
import requests

# This section imports the required Python modules: `requests`, `csv`, and `argv` from the `sys` module.

#get user_id from the command line arguements
user_id = argv[1]
# This line extracts the first command-line argument, which should be the user ID, and stores it in the variable `user_id`.

# Define the endpoint url to access a specific task
user_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
# This line constructs the URL for accessing the specific task data for the given `user_id`.

# Define the endpoint url for specific employee
user_details = f'https://jsonplaceholder.typicode.com/users/{user_id}'
# This line constructs the URL for accessing specific employee details for the given `user_id`.

# make API requests to retrieve the data
user_data = requests.get(user_details)
# This line sends an HTTP GET request to the `user_details` URL and stores the response in the `user_data` variable.

"""convert the data to json readable"""
user_json = user_data.json()
# This line parses the JSON data from the `user_data` response and stores it in the `user_json` variable.

# employeename
Name = user_json['username']
# This line extracts the 'username' field from the `user_json` data and stores it in the variable `Name`.

# retrieve the specific tasks for an employee
todos_response = requests.get(user_todos)
# This line sends an HTTP GET request to the `user_todos` URL and stores the response in the `todos_response` variable.

todos_data = todos_response.json()
# This line parses the JSON data from the `todos_response` response and stores it in the `todos_data` variable.

# initialize lists and counters
task_records = []
# This line initializes an empty list called `task_records` to store the task records.

# iterate through the todo items and count the completed and not completed data
for task in todos_data:
    task_id = task['id']
    # This line extracts the 'id' field from each task and stores it in the variable `task_id`.
    
    task_completed = task['completed']
    # This line extracts the 'completed' field from each task and stores it in the variable `task_completed`.
    
    task_title = task['title']
    # This line extracts the 'title' field from each task and stores it in the variable `task_title`.
    
    #  create a variabl
    row = f'"{user_id}","{Name}","{task_completed}","{task_title}"'
    task_records.append(row)
    # This line constructs a list containing the user ID, username, task completion status, and task title for each task,
    # and appends it to the `task_records` list.

#Define the CSV file name
csv_file = f'{user_id}.csv'
# write the data to a csv file
with open(csv_file, 'w', encoding='utf-8') as f:
    for row in task_records:
        f.write(row)
        f.write('\n')
    # writer = csv.writer(f)
    # writer.writerows(task_records)
# This section opens a CSV file named '2.csv' in write mode and writes the `task_records` data to the file using the `csv` module.

# The script essentially gathers information about a specific employee's tasks from an API and writes that information to a CSV file.