import pytest

from utils.fileUtils import getCsvDataAsDict, getDataAsTuple
from utils.apiUtils import postApiData
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
dataFile = 'registerApiData.csv'
urlPath = 'register'
dataFileWithStatus = 'registerApiDataWithStatus.csv'
getData = getDataAsTuple(dataFileWithStatus)

# datadriven test from datafile, inserting all data in single test
def test_dataDrivenRegApi():
    url = baseURI + urlPath
    payloadList = getCsvDataAsDict(dataFile)
    for dataLines in payloadList:
        print(dataLines)
        resp = postApiData(url, dataLines)
        assert resp.status_code == 201
        data = resp.json()
        print(data)
        assert data['id']



# datadriven test from datafile, uses Pytest paramterization, separate test for each row from data file
@pytest.mark.parametrize("input, respStatus", getDataAsTuple(dataFileWithStatus))
def test_dataDrivenParametrized(input, respStatus):
    url = baseURI + urlPath
    print (getData)
    print(input, respStatus)
    keys = ['email', 'password']
    requestDict = dict(zip(keys,input))
    print("Request Dict: ", requestDict, respStatus)
    #resp = postApiData(url, requestDict)
    #assert resp.status_code == int(respStatus)

