#!/usr/bin/python3

""" Export Employee Tasks to JSON

This Python script exports tasks owned by a specific employee in JSON format.
It retrieves task data for the specified user from a
remote API and saves it to a JSON file.

Usage:
    $ python script.py <user_id>
"""

# Import the necessary libraries
from sys import argv
import json
import requests

# Check for the correct number of command-line arguments
if len(argv) != 2:
    print("Usage: python3 gather_data_and_export_to_json.py <employee_id>")
    exit(1)

# Get the user_id from the command line arguments
user_id = argv[1]

# Define the endpoint URL to access specific todo items for the user
url_todos = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'

# Define the endpoint URL to get specific user details
url_user = f"https://jsonplaceholder.typicode.com/users/{user_id}"

# Make an API request to retrieve user data
user_data = requests.get(url_user)
user_info = user_data.json()
username = user_info['username']

# Make an API request to retrieve todo items for the user
todos_response = requests.get(url_todos)
todo_data = todos_response.json()

# Initialize lists and dictionary
data = []

# Iterate through the todo items and count completed and not completed tasks
for x in todo_data:
    tasks = {
        "task": x['title'],
        'completed': x['completed'],
        'username': username
    }
    data.append(tasks)

# Create a dictionary with the user's data
user_data = {
    'user_id': user_id,
    'username': username,
    'tasks': data
}

# Serializing JSON
json_object = json.dumps(user_data, indent=4)

# Create a JSON file using the user id
json_file = f'{user_id}.json'

# Writing to a JSON file
with open(json_file, 'w', encoding='utf-8') as f:
    f.write(json_object)
