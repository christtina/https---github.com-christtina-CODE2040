import requests
import json
import datetime
from datetime import timedelta


def stageOne():
    # creating api dictionary to be sent with the post request
    body = {'token': 'f0778fe18b809f724155cb0b431ace3f', 'github': 'https://github.com/christtina/CODE2040.git'}

    # making post request
    response = requests.post("http://challenge.code2040.org/api/register", json = body)

    # checking status code for debugging purposes
    print response.status_code
    print ("    " + response.content)
    return 0


def reverse():
    # creating api dictionary to be sent with the post request
    body = {'token': 'f0778fe18b809f724155cb0b431ace3f'}

    # making post request
    response = requests.post("http://challenge.code2040.org/api/reverse", json = body)

    # checking status code for debugging purposes
    print response.status_code

    # storing word to be reversed
    reverse = response.content
    print ("    String to be reversed: " + reverse)

    # reversing the string using python indexing properties
    reverse = reverse[::-1]
    print ("    Reversed string: " + reverse)

    # posting the answer to a new api
    body2 = {'token': 'f0778fe18b809f724155cb0b431ace3f', 'string': reverse}
    response2 = requests.post("http://challenge.code2040.org/api/reverse/validate", json = body2)

    return 0


def findNeedle():
    # creating api dictionary to be sent with the post request
    token = {'token': 'f0778fe18b809f724155cb0b431ace3f'}

    # making post request
    response = requests.post("http://challenge.code2040.org/api/haystack", json = token)

    # checking status code for debugging purposes
    print response.status_code

    # storing the dictionary the api sends and splitting it into needle & haystack
    dictionary = json.loads(response.content)
    needle = dictionary.get('needle')
    print ("    Needle: " + needle)
    haystack = dictionary.get('haystack')
    print "    Haystack: ",
    print haystack

    # finding the index of where needle is in the haystack
    index = haystack.index(needle)
    print "    index: " ,
    print index

    # posting the answer to a new api
    answer = {'token': 'f0778fe18b809f724155cb0b431ace3f', 'needle': index}
    response2 = requests.post("http://challenge.code2040.org/api/haystack/validate", json = answer)
    return 0

def findWords():
    # creating api dictionary to be sent with the post request
    token = {'token': 'f0778fe18b809f724155cb0b431ace3f'}

    # making post request
    response = requests.post("http://challenge.code2040.org/api/prefix", json = token)

    # checking status code for debugging purposes
    print response.status_code

    # storing the dictionary the api sends and splitting it into prefix and array
    dictionary = json.loads(response.content)
    prefix = dictionary['prefix']
    array = dictionary['array']
    print " Prefix: ",
    print prefix
    print " Array: ",
    print array

    # creating a new array that will hold
    n = len(prefix)
    newArray = []

    # adding the values in array that don't have the prefix to a new array
    for index in array:
    	if prefix != index[0:n] :
    		newArray.append(index)

    print " newArray: ",
    print newArray

    # posting the answer to a new api
    answer = {'token': 'f0778fe18b809f724155cb0b431ace3f', 'array' : newArray}
    response2 = requests.post("http://challenge.code2040.org/api/prefix/validate", json = answer)
    return 0

def dateInterval():
    # creating api dictionary to be sent with the post request
    token = {'token': 'f0778fe18b809f724155cb0b431ace3f'}

    # making post request
    response = requests.post("http://challenge.code2040.org/api/dating", json = token)

    # checking status code for debugging purposes
    print response.status_code

    # storing the dictionary the api sends and splitting it into interval and DT (datetime)
    dictionary = json.loads(response.content)
    interval = dictionary['interval']
    dt = dictionary['datestamp']
    DT = datetime.datetime.strptime( dt, '%Y-%m-%dT%H:%M:%SZ')
    print " interval: ",
    print interval
    print " Datestamp: ",
    print dt

    # finding the new time and adding it to the newTime variable
    newTime = DT + datetime.timedelta(0,interval)
    t = newTime.strftime("%Y-%m-%dT%H:%M:%SZ")
    print " NewTime: ",
    print t

    # posting the answer to a new api
    answer = {'token': 'f0778fe18b809f724155cb0b431ace3f', 'datestamp': t}
    response2 = requests.post("http://challenge.code2040.org/api/dating/validate", json = answer)
    return 0

print("Starting Stage 1...")
stageOne()

print("Starting Stage 2...")
reverse()

print("Starting Stage 3...")
findNeedle()

print("Starting Stage 4...")
findWords()

print("Starting Stage 5...")
dateInterval()
