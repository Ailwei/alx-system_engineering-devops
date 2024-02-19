#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees
"""

import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = "{}/{}".format(base_url, employee_id)

    # Fetch user data
    response = requests.get(user_url)
    if response.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)
    username = response.json().get('username')

    # Fetch TODO list data
    todo_url = "{}/{}/todos".format(base_url, employee_id)
    response = requests.get(todo_url)
    if response.status_code != 200:
        print("Error: Unable to fetch TODO list data")
        sys.exit(1)
    tasks = response.json()

    # Write to CSV file
    with open('{}.csv'.format(employee_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_id, username,
                        task.get('completed'),
                        task.get('title')
                        
                    ))


if __name__ == "__main__":
    main()
