#!/usr/bin/python3
# This is a shebang line indicating that this script should be run with Python 3.

"""
    A script that gathers data from an API
    and displays information about a 
    specific employee's task and exports it to JSON
"""
# This is a multi-line string (docstring) that provides a description of what the script does.
import json      # Import the 'json' module for working with JSON data.
import requests  # Import the 'requests' module for making HTTP requests.
from sys import argv  # Import the 'argv' variable from the 'sys' module for handling command-line arguments.

# Check for the correct number of command-line arguments
if len(argv) != 2:
    print("Usage: python3 gather_data_and_export_to_json.py <employee_id>")
    exit(1)  # Print a usage message and exit the script if the number of arguments is incorrect.

# Get user_id from the command line arguments
user_id = argv[1]  # Retrieve the user ID from the command-line argument.

# Define the endpoint URL to access a specific task
user_todos_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
# Construct the URL for accessing the specific tasks for the given user ID.

# Define the endpoint URL for specific employee details
user_details_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
# Construct the URL for accessing specific employee details for the given user ID.

try:
    # Make API requests to retrieve the data
    user_data = requests.get(user_details_url).json()
    # Send an HTTP GET request to retrieve user details and parse the JSON response.

    # Extract employee username
    username = user_data['username']
    # Extract the username from the user_data dictionary.

    # Retrieve the specific tasks for an employee
    todos_data = requests.get(user_todos_url).json()
    # Send an HTTP GET request to retrieve task data and parse the JSON response.

    # Initialize a dictionary to store task records
    task_records = {}
    #  create an empty list
    list = [] 
    # Create a dictionary with the user ID as the key and an empty list as the value.

    # Iterate through the todo items and create task records
    for task in todos_data:
        task_title = task['title']
        task_completed = task['completed']

        # Create a dictionary for each task
        task_record = {"task": task_title, "completed": task_completed, "username": username}
        # Create a dictionary with task details in the specified format.
        list.append(task_record)
        task_records[user_id] = list

        # task_records[user_id].append(task_record)
        # Append the task record to the list under the user ID key in the task_records dictionary.

    # Define the JSON file name
    json_file_name = f'{user_id}.json'
    # Construct the JSON file name based on the user's ID.

    # Export the data to a JSON file
    with open(json_file_name, 'w') as jsonfile:
        #  i need to print data continuously without indentation
        

        json.dump(task_records, jsonfile)
    # Write the task_records dictionary to a JSON file with proper formatting.

    print(f"Data has been exported to {json_file_name}")
    # Print a message indicating that the data has been exported.

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    exit(1)
# Handle exceptions related to HTTP requests and print an error message.