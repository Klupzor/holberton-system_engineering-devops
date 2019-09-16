#!/usr/bin/python3
"""Gather data from an API"""
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
            name = jsn.get('name')
        else:
            print("No result")
    task = "https://jsonplaceholder.typicode.com/todos?userId={}".format(uId)
    response = requests.get(task)
    cont = 0
    list_tasks = []
    tot = 0
    try:
        jsn = response.json()
    except BaseException:
        print("Not a valid JSON")
    else:
        if jsn:
            tot = len(jsn)
            for tasks in jsn:
                if tasks["completed"]:
                    list_tasks.append(tasks["title"])
                    cont += 1
        else:
            print("No result")
    print("Employee {} is done with tasks({}/{}):".format(name, cont, tot))
    for done in list_tasks:
        print("\t{}".format(done))
