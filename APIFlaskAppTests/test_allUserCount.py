from utils.apiUtils import getApiData
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
urlPath = 'allusercount'

# testing api all user count for status 200
def test_getAllUserCountStatus200():
    url = baseURI + urlPath
    headers = {'Accept': 'application/json'}
    resp = getApiData(url, headers)
    assert resp.status_code == 200

def test_getAllUserCountStatus406():
    url = baseURI + urlPath
    resp = getApiData(url)
    assert resp.status_code == 406


def test_getAllUserCountBody():
    url = baseURI + urlPath
    headers = {'Accept': 'application/json'}
    resp = getApiData(url, headers)
    data = resp.json()
    assert data['count']
    assert data['status']
    assert data['status']['message'] == 'success'

def test_getALlUserCountTimeTaken():
    url = baseURI + urlPath
    headers = {'Accept': 'application/json'}
    resp = getApiData(url, headers)
    print(resp.elapsed.total_seconds())
    assert (resp.elapsed.total_seconds()) < 1