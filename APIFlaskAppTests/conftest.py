import pytest
from utils.fileUtils import getJsonFromFile
from utils.apiUtils import postApiData, getApiData
from utils.myconfigparser import getFlaskAppBaseURL

loginJsonFile = 'loginValid.json'
baseURI = getFlaskAppBaseURL()
loginURLPath = 'login'


@pytest.fixture
def get_token():
    loginURL = baseURI + loginURLPath
    payload = getJsonFromFile(loginJsonFile)
    resp = postApiData(loginURL, payload)
    print(resp.json()['token'])
    token = resp.json()['token']
    yield token
