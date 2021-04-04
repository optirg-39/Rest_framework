import requests
import json

URL_1 = "http://127.0.0.1:8000/stucreate/"
data_1 = {
'city' : 'Meerut',
    'name' : 'Poonam',
'roll' : 100,
}
json_data = json.dumps(data_1)
rq = requests.post(url=URL_1,data=json_data)
print(rq)
rspo = rq.json()
print(rspo)