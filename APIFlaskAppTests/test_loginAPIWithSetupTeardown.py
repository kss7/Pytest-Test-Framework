import time
import pytest
import random
from utils.apiUtils import postApiData, delAPiData
from utils.fileUtils import getJsonFromFile
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
regUrlPath = 'register'
loginUrlPath = 'login'
delUrlPath = 'delete'
registerJsonFile = 'resgisterApiValid.json'
randNum = random.randint(0, 1000)
eMail = 'automateUser@auto' + str(randNum)
password ='1234'

@pytest.fixture(scope='module')
def reg_user():
    payload = getPayloadDict_RegAPI(eMail,password)
    regurl = baseURI + regUrlPath
    reg_response = postApiData(regurl, payload)
    assert reg_response.status_code == 201
    assert reg_response.json()['id']
    data = reg_response.json()
    print("Inside Fixture SETUP")
    yield data ## anything after this stmt, will run as part of teardown, or after the test function is executed.
    #time.sleep(5)
    print("Inside Fixture YIELD")
    delUrl = baseURI + delUrlPath
    loginUrl = baseURI + loginUrlPath
    login_resp = postApiData(loginUrl, payload)
    token = login_resp.json()['token']
    headers = {'x-access-token': token}
    payload = {"id": reg_response.json()['id']}
    del_resp = delAPiData(delUrl, payload, headers)
    assert del_resp.status_code == 200
    assert del_resp.json()['id'] == reg_response.json()['id']

def test_loginCorrectCreds(reg_user):
    payload = getPayloadDict_RegAPI(eMail, password)
    url = baseURI + loginUrlPath
    resp = postApiData(url, payload)
    assert resp.status_code == 200

def test_loginEmptyPassword(reg_user):
    regUserData = reg_user
    payload = getPayloadDict_RegAPI(eMail,'')
    url = baseURI + loginUrlPath
    resp = postApiData(url, payload)
    assert resp.status_code == 401




def getPayloadDict_RegAPI(email=None, pwd=None):
    payload = getJsonFromFile(registerJsonFile)
    payload['email'] = email
    payload['password'] = pwd
    return payload