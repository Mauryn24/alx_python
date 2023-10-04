#!/usr/bin/python3

"""
    Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
    NB: The endpoint for access specific TODO items for an employee with
    ID = 1 will be https://jsonplaceholder.typicode.com/users/1/todos, and the endpoint to get specific employee details will
    be https://jsonplaceholder.typicode.com/users/1
"""

# import the sys library
from sys import argv
# import the requests library
import requests


# Get the employee ID from the command line
employee_id = argv[1]

# Endpoint for accessing specific todo items
url_todos = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

# Endpoint for accessing specific employee details
url_user = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

# Send an HTTP GET request to the URL for TODO items
response = requests.get(url_todos)

# Parse the JSON response from the API
todos_data = response.json()

completed_tasks = []  # List to store completed task titles
total_tasks = len(todos_data)  # Total number of tasks

# Iterate through the TODO items
for task in todos_data:
    # Check if the task is completed
    if task['completed']:
        completed_tasks.append(task['title'])  # Add the title to the list of completed tasks

# Send an HTTP GET request to the URL for employee details
user_data = requests.get(url_user)
employee_data = user_data.json()

# Extract the employee's name
employee_name = employee_data['name']

# Print the employee's task progress and completed task titles
print("Employee {} is done with tasks ({}/{}):".format(employee_name, len(completed_tasks), total_tasks))
for title in completed_tasks:
    print("\t {}".format(title))