#!/usr/bin/python3

"""
    Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
    NB: The endpoint for access specific TODO items for an employee with
    ID = 1 will be https://jsonplaceholder.typicode.com/users/1/todos, and the endpoint to get specific employee details will
    be https://jsonplaceholder.typicode.com/users/1
"""

# import the requests library
import requests

# import the sys library
from sys import argv


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
















    meshack's

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