#!/usr/bin/python3
"""2-recurse."""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Get all hot posts for a subreddit.

    Args:
        subreddit (str): The subreddit name
        hot_list (list): The list of hot posts
        after (str): The last post ID

    Returns:
        list: The list of hot posts, or None if invalid subreddit.
    """
    if subreddit is None or type(subreddit) is not str:
        return None
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}
    hotInfo = requests.get(url,
                           headers={"User-Agent": "Python3"},
                           params=params)
    if hotInfo.status_code != 200:
        return None
    hotData = hotInfo.json().get("data", {})
    hotChildren = hotData.get("children", [])
    for child in hotChildren:
        hot_list.append(child.get("data", {}).get("title", ""))
    after = hotData.get("after", None)
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
