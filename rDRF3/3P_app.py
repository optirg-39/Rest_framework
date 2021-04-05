import requests
import json


# read operation
URL='http://127.0.0.1:8000/operation/'

def get_data():
    pass

def post_data():
    pass

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
delete_data()


