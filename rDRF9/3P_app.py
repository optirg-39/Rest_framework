import requests
import json


# read operation
URL='http://127.0.0.1:8000/studentapi/'

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id' : id}
    json_data = json.dumps(data)
    req = requests.get(url=URL, data = json_data)
    r = req.json()
    print(r)

get_data()

def post_data():
    data = {
        'id': 2,
        'name': 'rohit Batla',
        'city': 'khatauli',
        'roll': 1021,
    }
    headers_1 = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers = headers_1, data=json_data)
    save_respomse = r.json()
    print(save_respomse)

post_data()

def update_data():
    data = {
        'id':2,
        'name' : 'rohit Batla',
        'city' : 'khatauli',
        'roll' : 1021,
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL ,data = json_data)
    save_respomse = r.json()
    print(save_respomse)

# update_data()

def delete_data():
    data = {'id' : 2}
    json_data = json.dumps(data)
    r = requests.delete(url = URL ,data = json_data)
    save_respomse = r.json()
    print(save_respomse)
# delete_data()


