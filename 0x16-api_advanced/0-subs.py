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
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    aboutInfo = requests.get(url)
    subs = aboutInfo.json().get("data", {}).get("subscribers", 0)
    return subs
