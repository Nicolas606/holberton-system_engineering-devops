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

    data_csv = ''
    for dictionary in data_todos:
        data_csv += '"{}","{}","{}","{}"\n'.format(
            data_user.get('id'),
            data_user.get('username'),
            dictionary.get('completed'),
            dictionary.get('title')
        )

    with open(user_id + '.csv', 'w') as file:
        file.write(data_csv)
