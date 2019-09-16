#!/usr/bin/python3
"""Export to CSV"""
import requests
import sys, csv

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
            name = jsn.get('name')
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
                list_tasks.append(tasks["title"])
                status.append(tasks["completed"])
        else:
            print("No result")
    fileName = "{}.csv".format(uId)
    with open(fileName, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        for done, stat in zip(list_tasks, status):
             employee_writer.writerow([uId, name, stat, done])
