#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of
    subscribers """
import requests


def number_of_subscribers(subreddit):
    ''' returns the number of subscribers '''
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    json_reddit = requests.get(URL, allow_redirects=False)
    if  json_reddit.status_code == 200:
        return  json_reddit.json()['data']['subscribers']
    else:
        return 0
