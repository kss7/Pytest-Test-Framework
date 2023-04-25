import pytest
from utils.apiUtils import getApiData
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
urlPath = 'allusercount'

testData = [
    ('application/json', 200),
    ('application/xml', 406),
    ('multipart/mixed', 406),
    ('text/html', 406)
]

@pytest.mark.parametrize("type, status", testData)
def test_getAllUserCountStatus(type, status):
    url = baseURI + urlPath
    headers = {'Accept': type}
    resp = getApiData(url, headers)
    print(resp.status_code)
    assert resp.status_code == status