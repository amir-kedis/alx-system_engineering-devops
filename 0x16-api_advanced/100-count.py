#!/usr/bin/python3
"""100-count."""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Get the count of each word in word_list.

    Args:
        subreddit (str): The subreddit name
        word_list (list): The list of words to count
        after (str): The last post ID
        counts (dict): The count of each word

    Returns:
        dict: The count of each word, or None if invalid subreddit.
    """
    if not word_list or word_list == [] or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {"User-Agent": "Amir"}

    params = {"limit": 100}

    if after:
        params["after"] = after

    res = requests.get(url,
                 headers=headers,
                 params=params,
                 allow_redirects=False)

    if res.status_code != 200:
        return

    main_data = res.json()
    data = main_data.get("data")
    children = data.get("children")

    for post in children:
        title = post.get("data", {}).get("title").lower();

        for word in word_list:
            if word.lower() in title:
                counts[word] = counts.get(word, 0) + title.count(word.lower())
    
    after = main_data.get("data", {}).get("after")
    
    if after:
        count_words(subreddit, word_list,after, counts)
    else:
        sorted_counts = sorted(counts.items(),
                               key=lambda x: (-x[1], x[0].lower))
        for word,count in sorted_counts:
            print(f"{word.lower()}: {count}")

                                


