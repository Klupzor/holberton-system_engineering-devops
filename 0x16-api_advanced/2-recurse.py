#!/usr/bin/python3
"""Gather data from an reddit API"""
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """Gather data from an reddit API"""
    base_url = "https://www.reddit.com"
    url = base_url + "/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Andres'}
    params = {'limit': 100, 'after': after}
    response = requests.get(
        url,
        params=params,
        headers=headers,
        allow_redirects=False)

    if response.status_code != 200:
        return (None)
    jsn = response.json()
    posts = jsn.get("data").get("children")
    for post in posts:
        hot_list.append(post.get("data").get("title"))
    after = jsn.get("data").get("after")
    if after is not None:
        recurse(subreddit, hot_list, after)
    return (hot_list)
