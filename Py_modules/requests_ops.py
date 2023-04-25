import requests, json

url = 'https://www.google.com/search?q=pytest'
r = requests.get(url)
#print(r.text)

url = 'https://reqres.in/api/users'
r = requests.get(url)
print(r.status_code)
print(r.headers)
print(r.request.headers)
print(r.text)
print(r.json())
print(r.headers['Content-Type'])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

URL = 'https://httpbin.org/get'
myparams = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(URL, params=myparams)
print(r.url)

for key, value in r.json().items():
    print(key, ":", value)
print(r.json()["headers"]["Host"])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

URL = 'http://httpbin.org/post'
payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'accept': 'application/json', 'Content-Type': 'application/json' }
r = requests.post(URL, json=payload, headers=headers)
print(r.url)
print(r.status_code)
print(r.text)
print(r.request.headers)
print(r.headers)