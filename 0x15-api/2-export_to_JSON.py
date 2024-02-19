#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    response = requests.get(url)
    username = response.json().get('username')

    todo_url = f"{url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    user_tasks = [
            {"task": task.get('title'),
                "completed": task.get('completed'),
                "username": username} for task in tasks]

    with open(f'{employee_id}.json', 'w') as file:
        json.dump({employee_id: user_tasks}, file, indent=4)
    print(f'{employee_id}.json')
