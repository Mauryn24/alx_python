#!/usr/bin/python3
"""
This script gathers data from an API
and displays information about a specific
employee's tasks."""

# Import the necessary libraries
import json
import requests

# Define the endpoint URL to get specific employee details
url_user = "https://jsonplaceholder.typicode.com/users"

# Make an API request to retrieve user data
user_data = requests.get(url_user)
user_details = user_data.json()

# Create an empty dictionary to store user tasks
user_tasks = {}

# Iterate through the user details
for user in user_details:
    user_id = user['id']
    username = user['username']

    # Define the endpoint URL to access specific todo items for the user
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    # Make an API request to retrieve todo items for the user
    todos_response = requests.get(url_todos)
    todo_data = todos_response.json()

    # Initialize a list to store tasks for this user
    tasks = []

    # Iterate through the todo items and add them to the tasks list
    for x in todo_data:
        task_info = {
            "username": username,
            "task": x['title'],
            "completed": x['completed'],
        }
        tasks.append(task_info)

# Add the tasks list to the user_tasks dictionary with the user_id as the key
        user_tasks[f'{user_id}'] = tasks

    # Serializing JSON
json_object = json.dumps(user_tasks)

with open('todo_all_employees.json', 'w', encoding='utf-8', newline='') as f:
    f.write(json_object)