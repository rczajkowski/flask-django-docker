import json
import requests

from settings import URL_FOR_API_USER


class User():

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_all_users(self):
        r = requests.get(URL_FOR_API_USER)
        users = r.json()
        users_dict = json.dumps(users)
        all_users = json.loads(users_dict)['objects']

        return all_users

    def save_user(self):
        data = json.dumps({u'username': self.username, u'password': self.password})
        headers = {'content-type': 'application/json'}
        request = requests.post(url=URL_FOR_API_USER, data=data, headers=headers)

        return request