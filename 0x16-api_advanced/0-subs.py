#!/usr/bin/python3
"""Gather data from an reddit API"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Gather data from an reddit API"""
    base_url = "https://www.reddit.com"
    url = base_url + "/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'Andres'}
    response = requests.get(url, headers=headers)
    if response.status_code is not 200:
        return (0)
    try:
        jsn = response.json()
    except BaseException:
        print("Not a valid JSON")
    else:
        if jsn:
            return (jsn.get("data").get("subscribers"))
        else:
            return (0)
