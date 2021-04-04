import requests

lur = 'http://127.0.0.1:8000/stude_info'

r = requests.get(url=lur)

data = r.json()

print(data)