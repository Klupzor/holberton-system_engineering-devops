#!/usr/bin/python3
"""Gather data from an reddit API"""
import requests
import sys


def top_ten(subreddit):
    """Gather data from an reddit API"""
    base_url = "https://www.reddit.com"
    url = base_url + "/r/{}/hot.json?limit=10".format(subreddit)
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
            posts = jsn.get("data").get("children")
            for post in posts:
                print(post.get("data").get("title"))
        else:
            return (0)
