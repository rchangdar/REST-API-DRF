import requests
import json

URL = "http://127.0.0.1:8000/empcreate/"

data = {
    
    'empid' : 2569038,
    'name':'Sanket Kumar',
    'city':'Patna',
    'zip':340001
}

# Need to convert python dictionary into json

json_data = json.dumps(data)

r = requests.post(url = URL, data = json_data)
#data = r.json()

#print(data) 