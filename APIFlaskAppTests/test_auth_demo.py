from utils.fileUtils import getJsonFromFile
from utils.apiUtils import postApiData, getApiData
from utils.myconfigparser import getFlaskAppBaseURL

loginJsonFile = 'loginValid.json'
baseURI = getFlaskAppBaseURL()
loginURLPath = 'login'
usersUrlPath = 'users'

# demo test with fetch token within test
def test_getUsersDemo():
    #first login with and existing user
    loginURL = baseURI + loginURLPath
    payload = getJsonFromFile(loginJsonFile)
    resp = postApiData(loginURL, payload)
    print(resp.json()['token'])
    token = resp.json()['token']
    userURL = baseURI + usersUrlPath
    headers = {'x-access-token': token}
    resp_users = getApiData(userURL, headers)
    print(resp_users.json())