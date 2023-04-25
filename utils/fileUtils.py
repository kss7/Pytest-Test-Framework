import csv
import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
TEST_DATA_DIR = BASE_DIR.joinpath('TestData')

def getJsonFromFile(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as file:
        return json.load(file)

# function to read data from CSV file
def getCsvDataAsDict(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as file:
        csvFile = csv.DictReader(file)
        dictList = list(csvFile)
    return dictList

#get data from CSV as list
def getDataAsList(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        lines = list(reader)
    return lines

# returns list of tuples, Within tuples its "list of inputs" and a scalar value for output-status
def getDataAsTuple(filename):
    dataList = getDataAsList(filename)
    newList = []
    for lines in dataList:
        newList.append((lines[:2], lines[2]))
    #[expression(element) for element in oldList if condition]
    #newList2 = [(x[:2],x[2]) for x in dataList]
    return newList



print('~~~~~~~~~~~~~')
#print(getCsvDataAsDict('registerApiData.csv'))

#print(getDataAsList('registerApiDataWithStatus.csv'))

## WE can create a dict with list of zipped keys and values
keys = ['a', 'b', 'c', 'd']
values = ['alpha', 'beta', 'delta']
d = dict(zip(keys, values))
print(d)

