#!/usr/bin/python3
"""Get top ten hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """
    Get top ten hot posts for a subreddit.

    Args:
        subreddit (str): The subreddit name

    Returns:
        None: If invalid subreddit or no hot posts.
    """
    if subreddit is None or type(subreddit) is not str:
        print(None)
        return

    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    hotInfo = requests.get(url)
    hotPosts = hotInfo.json().get("data", {}).get("children", [])

    if len(hotPosts) == 0:
        print(None)
        return
    for i in range(10):
        print(hotPosts[i].get("data", {}).get("title", ""))
