import requests
import json

URL = "http://127.0.0.1:8000/empcreate/"

data = {
    
    'empid' : 2569032,
    'name':'Soura Das',
    'city':'Delhi',
    'zip':349656
}

# Need to convert python dictionary into json

json_data = json.dumps(data)

r = requests.post(url = URL, data = json_data)
#data = r.json()

#print(data) 