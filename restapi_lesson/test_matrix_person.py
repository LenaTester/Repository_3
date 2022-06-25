import json
from http import HTTPStatus

import requests
from requests import get, post

from restapi_lesson.config import config
from restapi_lesson.matrix_person_api import MatrixPersonAPI
from restapi_lesson.matrix_person_class import MatrixPerson

def test_post_matrix_person():
    '''post new matrix person - 7'''
    url = f"{config['base_url']}/api/users"
    new_matrix_person = {"name": "Morpheus", "job": "leader"}
    response = requests.post(url, json=new_matrix_person)
    assert response.reason == 'Created'
    assert response.status_code == HTTPStatus.CREATED, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.Created}'

def test_update_through_post_matrix_person():
    '''update matrix person through post - new name - 200 - 8'''
    url = f"{config['base_url']}/api/users/2"
    new_name = {"name": "Neo", "job": "leader"}
    response = requests.put(url, json=new_name)
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'

def test_update_through_patch_matrix_person():
    '''update matrix person through patch - new name - 200 - 9'''
    url = f"{config['base_url']}/api/users/2"
    new_name = {"name": "Trinity"}
    response = requests.patch(url, json=new_name)
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'

def test_delete_matrix_person():
    '''delete matrix person - 204 - 10'''
    url = f"{config['base_url']}/api/users/2"
    response = requests.delete(url)
    assert response.reason == 'No Content'
    assert response.status_code == HTTPStatus.NO_CONTENT, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.NO_CONTENT}'

