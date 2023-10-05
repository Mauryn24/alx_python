#!/usr/bin/python3

"""
    Export Employee Tasks to JSON

    This Python script exports tasks owned by a specific employee in JSON format.
    It retrieves task data for the specified user from a
    remote API and saves it to a JSON file.

    Usage:
        $ python script.py <user_id>
"""

# Import the necessary libraries
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

# Initialize a list to store task records
task_records = []

# Iterate through the todo items and create task records
for task in todo_data:
    task_title = task['title']
    task_completed = task['completed']

    # Create a dictionary for each task in the specified format
    task_record = {"task": task_title,
                   "completed": task_completed, "username": user_id}

    task_records.append(task_record)

# Define the JSON file name
json_file_name = f'{user_id}.json'

# Export the data to a JSON file
with open(json_file_name, 'w') as jsonfile:
    json.dump(task_records, jsonfile, indent=4)

print(f"Data has been exported to {json_file_name}")
