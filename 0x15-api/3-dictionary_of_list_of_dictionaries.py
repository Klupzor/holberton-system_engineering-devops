#!/usr/bin/python3
"""Export to JSON"""
import json
import requests

if __name__ == "__main__":
    request = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(request)
    try:
        users = response.json()
    except BaseException:
        print("Not a valid JSON")
    request = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(request)
    try:
        tasks = response.json()
    except BaseException:
        print("Not a valid JSON")
    to_dict = {}
    for user in users:
        values = []
        user_id = user.get("id")
        for task in tasks:
            if task.get("userId") == user_id:
                values.append({"task": task.get("title"),
                               "completed": task.get("completed"),
                               "username": user.get("username")})
        to_dict.update({user_id: values})

    fileName = "todo_all_employees.json"
    with open(fileName, 'w') as employee_file:
        json.dump(to_dict, employee_file)
