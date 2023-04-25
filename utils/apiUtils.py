import requests, json

def getApiData(url , opHeader=None):
    headers = {'Content-Type': 'application/json'}
    headers = (headers | opHeader) if isinstance(opHeader, dict) else headers
    response = requests.get(url, verify=False, headers=headers)
    print("\nRequestURL: " + url)
    print("request header:", response.request.headers)
    print("response header:", response.headers)
    return response

def postApiData(url, body):
    headers = {'Content-Type': 'application/json'}
    print("\nReqURL:" + url)
    print("ReqBody: " + json.dumps(body))
    return requests.post(url, verify=False, json=body, headers=headers)

def delAPiData(url, body, opHeader=None):
    headers = {'Content-Type': 'application/json'}
    headers = (headers | opHeader) if isinstance(opHeader, dict) else headers
    print("\nReqURL:" + url)
    print("ReqBody: " + json.dumps(body))
    response = requests.delete(url, json=body, headers=headers)
    return response