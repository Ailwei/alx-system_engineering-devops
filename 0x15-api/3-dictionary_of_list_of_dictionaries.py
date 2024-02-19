#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees
"""


import json
import requests
from collections import defalultdict


def fetch_todo_data(employee_id):
    """
    fetch_todo_ data
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    response = requests.get(url)
    user_data = response.json()
    username = user_data.get('username')

    todo_url = f"{url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    return {"username": username, "tasks": tasks}


def export_to_json(file):
    """
    export to json
    """
    all_employees_data = defaultdict(list)

    for employee_id in range(1, 11):
        employee_data = fetch_todo_data(employee_id)
        all_employees_data[employee_id] = employee_data

    with open(filename, 'w') as file:
        json.dump(all_employees_data, file, indent=4)


if __name__ == '__main__':
    export_to_json('todo_all_employees.json')
