#!/usr/bin/python3

"""
    A script that gathers data in an API
    and displays information about a 
    specific employee's task
"""

# import the necessary modules
import requests
import sys

#get user_id from the command line arguements
user_id = sys.argv[1]

# Define the endpoint url to access a specific task
user_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

# Define the endpoint url for specific employee
user_details = f'https://jsonplaceholder.typicode.com/users/{user_id}'

# make API requests to retrieve the data
user_data = requests.get(user_details)

"""convert the data to json readable"""
user_json = user_data.json()

# employeename
Name = user_json['name']

# retrieve the specific tasks for an employee
todos_response = requests.get(user_todos)
todos_data = todos_response.json()

#initialize lists and counters
titles = []
completed = 0
totalTasks = 0

# iterate through the todo items and count the completed and not completed data
for x in todos_data:
    if (x['completed'] == True):
        completed += 1
        titles.append(x['title'])
    if (x['completed'] == False or x['completed'] == True):
        totalTasks += 1

# Display the employee's Task information
print(f'Employee {Name} is done with tasks({completed}/{totalTasks}):')

#print the titles of completed tasks with indentation and spacing
for title in titles:
    print(f'\t {title}')