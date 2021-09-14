#!/usr/bin/python3
"""  Python script to export data in the JSON format."""

import json
import requests

if __name__ == '__main__':
    https = 'https://jsonplaceholder.typicode.com/'
    response = requests.get("{}users".format(https))
    data_user = response.json()
    response = requests.get("{}todos".format(https))
    data_todos = response.json()

    dictionary = {}
    output = {}
    new_list = []

    for user in data_user:
        for dic in data_todos:
            if dic['userId'] == user['id']:
                dictionary['task'] = dic['title']
                dictionary['completed'] = dic['completed']
                dictionary['username'] = user['username']
                new_list.append(dictionary)
        output[user.get('id')] = new_list

    with open('todo_all_employees.json', mode='w') as file:
        json.dump(output, file)
