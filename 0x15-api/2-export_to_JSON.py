#!/usr/bin/python3
"""  Python script to export data in the JSON format."""

import json
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

    dictionary = {}
    output = {}
    new_list = []

    for dic in data_todos:
        if dic['userId'] == int(argv[1]):
            dictionary['task'] = dic['title']
            dictionary['completed'] = dic['completed']
            dictionary['username'] = data_user['username']
            new_list.append(dictionary)

    output[user_id] = new_list

    with open(user_id + '.json', mode='w') as file:
        json.dump(output, file)
