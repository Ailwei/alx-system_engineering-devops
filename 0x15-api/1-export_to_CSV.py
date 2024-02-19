#!/usr/bin/python3
"""
Python script to export data in CSV format,
you can use the csv module in Python.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Fetch user data
    user_url = '{}users/{}'.format(base_url, employee_id)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO list data
    todo_url = '{}todos?userId={}'.format(base_url, employee_id)
    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print("Error: Unable to fetch TODO list data")
        sys.exit(1)
    todo_data = todo_response.json()

    # Export data to CSV file
    csv_filename = '{}.csv'.format(employee_id)
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            writer.writerow([
                employee_id,
                employee_name,
                '{}'.format(task['completed']),
                task['title']
            ])
    
    print("Data exported to:", csv_filename)
