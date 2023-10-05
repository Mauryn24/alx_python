#!/usr/bin/python3
"""
This script gathers data from an API
and displays information about a specific
employee's tasks."""

# Import the necessary libraries
import requests
from sys import argv

# Get the user_id from the command line arguments
user_id = argv[1]

# Define the endpoint URL to access specific todo items for the user
url_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

# Define the endpoint URL to get specific employee details
url_user = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

# Make an API request to retrieve user data
user_data = requests.get(url_user)
res = user_data.json()
employeeName = res['name']

# Make an API request to retrieve todo items for the user
todos_response = requests.get(url_todos)
todo_data = todos_response.json()

# Initialize lists and counters
titles = []
completed = 0
totalTasks = 0

# Iterate through the todo items and count completed and not completed tasks
for x in todo_data:
    if (x["completed"] == True):
        completed += 1
        titles.append(x['title'])
    if (x['completed'] == False or x['completed'] == True):
        totalTasks += 1

# Display the employee's task information
print('Employee {} is done with tasks({}/{}):'
      .format(employeeName, completed, totalTasks))

# Display the titles of completed tasks with indentation
for title in titles:
    print(f'\t {title}')