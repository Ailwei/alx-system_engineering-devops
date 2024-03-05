#!/usr/bin/python3
"""
 recursive function that queries the Reddit API,
 parses the title of all hot articles, and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list):
    """
    cont words
    """
    if subreddit is None or not isinstance(subreddit, str):
        return

    user_agent = {'User-agent': 'Custom User Agent'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            word_count = {}
            for post in posts:
                title = post['data']['title']
                for word in word_list:
                    word = word.lower()
                    if word in title.lower():
                        if word in word_count:
                            word_count[word] += title.lower().count(word)
                        else:
                            word_count[word] = title.lower().count(word)
            if not word_count:
                return

            sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
        else:
            return
    except Exception as e:
        print("Error:", e)
        return
