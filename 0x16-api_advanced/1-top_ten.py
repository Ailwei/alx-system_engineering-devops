#!/usr/bin/python3
"""
function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-agent': 'Custom User Agent'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print("None")
    except Exception as e:
        print("Error:", e)
