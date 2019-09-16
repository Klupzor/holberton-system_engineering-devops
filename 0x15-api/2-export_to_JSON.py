#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) is not 2:
        raise SyntaxError("Id is necessary")
    uId = sys.argv[1]
    user = "https://jsonplaceholder.typicode.com/users/{}".format(uId)
    response = requests.get(user)
    name = ""
    try:
        jsn = response.json()
    except BaseException:
        print("Not a valid JSON")
    else:
        if jsn:
            name = jsn.get('username')
        else:
            print("No result")
    task = "https://jsonplaceholder.typicode.com/todos?userId={}".format(uId)
    response = requests.get(task)
    list_tasks = []
    status = []
    tot = 0
    try:
        jsn = response.json()
    except BaseException:
        print("Not a valid JSON")
    else:
        if jsn:
            tot = len(jsn)
            for tasks in jsn:
                list_tasks.append(tasks.get("title"))
                status.append(tasks.get("completed"))
        else:
            print("No result")
    values = []
    val = {}
    for done, stat in zip(list_tasks, status):
        values.append({"task": done, "completed": stat, "username": name})
    to_dict = {uId: values}

    fileName = "{}.json".format(uId)
    with open(fileName, 'w') as employee_file:
        json.dump(to_dict, employee_file)
