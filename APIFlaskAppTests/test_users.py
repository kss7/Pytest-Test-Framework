import json

import pytest
from utils.fileUtils import getJsonFromFile
from utils.apiUtils import postApiData, getApiData
from utils.myconfigparser import getFlaskAppBaseURL

#loginJsonFile = 'loginValid.json'
baseURI = getFlaskAppBaseURL()
#loginURLPath = 'login'
usersUrlPath = 'users'

# @pytest.fixture
# def get_token():
#     loginURL = baseURI + loginURLPath
#     payload = getJsonFromFile(loginJsonFile)
#     resp = postApiData(loginURL, payload)
#     print(resp.json()['token'])
#     token = resp.json()['token']
#     yield token

#test get users with fixtures
def test_getUsers(get_token):
    token = get_token
    usersURL = baseURI + usersUrlPath
    headers = {'x-access-token': token}
    resp_users = getApiData(usersURL, headers)
    print(json.dumps(resp_users.json(), indent=4))
    assert resp_users.json()['users'][0]['email']