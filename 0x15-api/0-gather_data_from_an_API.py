#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Retrieve information about the employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing the employee name, number of completed tasks,
               total number of tasks, and a list of completed task titles.
    """
    # Fetch user data
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    if user_response.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch TODO list data
    todo_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    if todo_response.status_code != 200:
        print("Error: Unable to fetch TODO list data")
        sys.exit(1)
    todo_data = todo_response.json()

    # Process TODO list progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])
    done_tasks = [task['title'] for task in todo_data if task['completed']]

    return employee_name, completed_tasks, total_tasks, done_tasks

def display_employee_todo_progress(employee_name, completed_tasks, total_tasks, done_tasks):
    """
    Display the employee's TODO list progress.

    Args:
        employee_name (str): The name of the employee.
        completed_tasks (int): The number of completed tasks.
        total_tasks (int): The total number of tasks.
        done_tasks (list): A list of completed task titles.
    """
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for task_title in done_tasks:
        print("\t", task_title)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    employee_name, completed_tasks, total_tasks, done_tasks = get_employee_todo_progress(employee_id)
    display_employee_todo_progress(employee_name, completed_tasks, total_tasks, done_tasks)
