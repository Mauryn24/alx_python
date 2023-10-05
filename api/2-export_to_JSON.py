#!/usr/bin/python3


""" 
    Export Employee Tasks to JSON

    This Python script exports tasks owned by a specific employee in JSON format.
    It retrieves task data for the specified user from a
    remote API and saves it to a JSON file.

    Usage:
        $ python script.py <user_id>
"""


import json
import requests
from sys import argv

# Check for the correct number of command-line arguments
if len(argv) != 2:
    print("Usage: python3 gather_data_and_export_to_json.py <employee_id>")
    exit(1)

# Get the user_id from the command line arguments
user_id = argv[1]

# Define the endpoint URL to access specific todo items for the user
url_todos = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'

# Make an API request to retrieve todo items for the user
todos_response = requests.get(url_todos)
todo_data = todos_response.json()

# Initialize dictionary to store tasks for the user
user_tasks = {}

# Iterate through the todo items and store them in the dictionary
for task in todo_data:
    task_title = task['title']
    task_completed = task['completed']

    # Create a dictionary for the task
    task_dict = {"task": task_title, "completed": task_completed}

    # Append the task to the list of tasks for the user
    user_tasks[user_id] = task_dict

# Read existing data from JSON file
with open('todo_all_employees.json', 'r') as json_file:
    all_user_tasks = json.load(json_file)

# Add the user's tasks to the existing data
all_user_tasks[user_id] = user_tasks

# Write the updated data to the JSON file
with open('todo_all_employees.json', 'w') as json_file:
    json.dump(all_user_tasks, json_file)