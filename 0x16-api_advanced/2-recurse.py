#!/usr/bin/python3
"""
ecursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    user_agent = {'User-agent': 'Custom User Agent'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    if after:
        url += f'&after={after}'

    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        print("Error:", e)
        return None
