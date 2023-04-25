import json

dataDict = {
    "sampleString": "Great Automation Framework",
    "sampleList": ["Good", "Better", "Best"],
    "sampleTuple": ("Python", "Pytest", "Automation"),
    "sampleObj": {"platform": "Udemy", "Valuable": True},
    "sampleInteger": 555,
    "booleanValue": True,
    "noneValue": None
}

print("Convert py dict to JSON")
resultJSON = json.dumps(dataDict, sort_keys=True, indent=4)
#print(resultJSON)
print(type(resultJSON) == str)
data_dict = json.loads(resultJSON)
print(type(data_dict))

with open("example.json", "r") as file:
    data = json.load(file)
    print(type(data))
    print(data.keys())
    print(type(data['address']))
    print(type(data['hobbies']))

    for key, value in data.items():
        print(key, ":", value)

def validateJSON(jsonStr):
    try:
        json.loads(jsonStr)
    except ValueError as err:
        return False
    return True

JsonString = """{"name": "Raji", "salary": 25000, "email": "raji@mymail.com"}"""
isValid = validateJSON(JsonString)
print("Json string passed is valid?", isValid)