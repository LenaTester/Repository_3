from pythonProject.Repository_3.restapi_lesson.utilities.config import config
import requests


class BaseAPI:

    def __init__(self):
        self.base_url = config['base_url']
        self.user = 'Lena'
        self.headers = None
        self.request = requests

    def get(self, url, body=None, headers=None, params=None):
        print('GET from BaseAPI')
        if headers is None:
            print('BASE HEADERS')
            headers = self.headers
        else:
            print('CUSTOM_HEADERS')
        response = self.request.get(f"{self.base_url}{url}", data=body, headers=headers, params=params)
        print(f'Perform GET request')
        return response

    def post(self, url, body=None, headers=None, params=None):
        print('GET from BaseAPI')
        if headers is None:
            headers = self.headers
        response = self.request.post(f"{self.base_url}{url}", data=body, headers=headers, params=params)
        print(f'Perform POST request')
        return response
