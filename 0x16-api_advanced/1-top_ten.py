#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of
    subscribers """
import requests


def top_ten(subreddit):
    ''' returns the number of subscribers '''
    URL = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'my-app/0.0.1'}
    json_reddit = requests.get(URL, headers=headers, allow_redirects=False)
    if json_reddit.status_code == 200:
        for i in json_reddit.json()['data']['children']:
            print(i['data']['title'])
    else:
        print('None')
