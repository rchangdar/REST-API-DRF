import requests
import json
URL = ""

data = {
    
    'empid' : '111000',
    'name':'Krishnendu Jana',
    'city':'Allahabad',
    'zip':894523
}

# Need to convert python dictionary into json

json_data = json.dumps(data)

r = requests.post(url = URL, data = json_data)
data = r.json()

print(data) 