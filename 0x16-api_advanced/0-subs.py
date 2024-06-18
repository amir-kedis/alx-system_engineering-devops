#!/usr/bin/python3
"""Gets the number of subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """
    Get number of subscribers for a subreddit.

    Args:
        subreddit (str): The subreddit name

    Returns:
        int: The number of subscribers for the subreddit,
        0 if invalid subreddit.
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = f"http://www.reddit.com/r/{subreddit}/about.json"

    res = requests.get(url, headers={"User-Agent": "Amir"},
                       allow_redirects=False)
    if (res.status_code != 200):
        return 0

    subs = res.json().get("data", {}).get("subscribers", 0)

    return subs
