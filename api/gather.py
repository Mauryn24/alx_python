#!/usr/bin/python

"""
    Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
    NB: The endpoint for access specific TODO items for an employee with
    ID = 1 will be https://jsonplaceholder.typicode.com/users/1/todos and the endpoint to get specific employee details will
    be https://jsonplaceholder.typicode.com/users/1
"""

# import the requests library
import requests
# import the sys library
import sys

# get the employee ID from the command line
user_id = sys.argv[1]

# endpoint for access specific todo items
url_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

# endpoint for access specific employee details
url_user = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

# Send an HTTP GET request to the URL for TODO items
response = requests.get(url_todos)

# Parse the JSON response from the API
res = response.json()

completed = 0
notCompleted = 0

# Iterate through the TODO items
for x in res:
    # Check if the task is not completed
    if not x['completed']:
        notCompleted += 1
    else:
        # If the task is completed, increment the completed count
        completed += 1
        totalTasks = completed + notCompleted

    # Store the title of the completed task (only the last one will be stored)
    if x['completed']:
        TASK_TITLE = x['title']

# Send an HTTP GET request to the URL for employee details
user_data = requests.get(url_user)
res = user_data.json()

# Extract the employee's name
employeeName = res['name']

# Print the employee's task progress and completed task title
print("Employee {} is done with tasks({}/{}):".format(employeeName, completed, totalTasks))
print("\t {}".format(TASK_TITLE))