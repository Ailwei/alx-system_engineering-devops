#!/usr/bin/python3
"""
Python script that retrieves information about an employee's TODO list progress
using a REST API.

Requirements:
- The script must accept an integer as a parameter, which is the employee ID.
- Script must display on the standard output the employee TODO list progress
  in the following format:
    - First line: "Employee EMPLOYEE_NAME is done with taskS"
      - EMPLOYEE_NAME: name of the employee
      - NUMBER_OF_DONE_TASKS: number of completed tasks
      - TOTAL_NUMBER_OF_TASKS: total number of tasks,
      which is the sum of completed and non-completed tasks
    - Second and N next lines display the title of completed tasks:
    "TASK_TITLE"
"""

import requests
import sys

if __name__ =="__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch user data
    user_response = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id
                )
            )
    if user_response.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO list data
    todo_response = requests.get
    (
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
            )
    if todo_response.status_code != 200:
        print("Error: Unable to fetch TODO list data")
        sys.exit(1)
    todo_data = todo_response.json()

    # Process TODO list process
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])
    done_tasks = [task['title'] for task in todo_data if task['completed']]

    # Display progress
    print(
            "Employee {} is done with tasks({}/{}):".format(
                employee_name, completed_tasks, total_tasks
                )
            )
    for task in done_tasks:
        print("\t", task)
