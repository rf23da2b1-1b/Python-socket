import requests

URL = 'http://localhost:5106/api/Pizzas/'

def GetAll():
    response = requests.get(URL)
    data = response.json()
    return data, response

def Add(item):
    response = requests.post(URL, json=item)
    return response
    