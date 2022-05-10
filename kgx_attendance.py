from datetime import datetime
import requests
import json
d =	{}
key = input()

url_post = "https://intent-sunbeam-40.hasura.app/api/rest/entry"
url_update = "https://intent-sunbeam-40.hasura.app/api/rest/update_attendance"


headers = {"Content-Type": "application/json; charset=utf-8", "x-hasura-admin-secret" : "4E9fBl6pQoyEL138Ov9jmoY3xnKtMpKm2KtrHWHPOUdcXzMHBzvII9CDooZZH5Ay"}

data_in_time = {
    "attendance":{
        "rfid_key": key,
        "in_time" : "2003-04-12 04:05:06"
    }
}

data_out_time = {
    "id": 37,
    "out_time": "2003-04-12 04:05:06"
}

if key in d:
  update = requests.patch(url_update, headers=headers, json=data_out_time)
  del d[key]
else:
    response = requests.post(url_post, headers=headers, json=data_in_time)
    d[key].append(response)

 
print("Status Code", response.status_code)
print("JSON Response ", response.json())

print(d)

  
