#!/usr/bin/python3
""" Python script to export data in the CSV format."""

import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    https = 'https://jsonplaceholder.typicode.com/'
    response = requests.get(https + 'users/' + user_id)
    data_user = response.json()
    response.close()

    response = requests.get(https + 'users/' + user_id + '/todos')
    data_todos = response.json()
    response.close()

with open(user_id + '.csv', mode='w') as file:
    for task in data_todos:
        file.write('"{}","{}","{}","{}"\n'.format(
            data_user.get('id'),
            data_user.get('username'),
            task.get('completed'),
            task.get('title')
        ))
