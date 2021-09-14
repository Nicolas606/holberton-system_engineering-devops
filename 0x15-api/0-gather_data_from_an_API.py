#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID, returns
    information about his/her TODO list progress.
"""

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
    tasks = ''
    tasks_count = 0
    for task in data_todos:
        if task.get('completed'):
            tasks += '\t {}\n'.format(task.get('title'))
            tasks_count += 1

    print('Employee {} is done with tasks({}/{}):'.format(
        data_user.get('name'),
        tasks_count,
        len(data_todos))
    )
    print(tasks, end='')
