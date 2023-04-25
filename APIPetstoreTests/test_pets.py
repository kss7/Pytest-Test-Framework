from utils.myconfigparser import *
from utils.myutils import getAPIData, putData, deleteData
import logging
LOGGER = logging.getLogger(__name__)

#baseURI = 'https://petstore.swagger.io/v2/pet/'
petID = '191'
baseURI = getPetAPIURL()

def test_getPetById_response():
    url = baseURI + petID
    data, resp_status, timeTaken = getAPIData(url)
    assert data['id'] == int(petID)
    assert resp_status == 200
    print("Time Taken: ", timeTaken)


# test updating a pet
def test_updatingPet():
    payload = {"id": int(petID), "name": "Cutie", "status": "pending"}
    data, resp_status, timeTaken = putData(baseURI, payload)
    LOGGER.info("API call done")
    assert data['id'] == int(petID)
    print(data)

# test deleting a pet
def test_deletePetById():
    url = baseURI + petID
    apiKey = {'api_key' : 'apiKeys123'}
    data, resp_status, timeTaken = deleteData(url, apiKey)
    print(data)
    assert data['message'] == petID
    assert data['code'] == 200