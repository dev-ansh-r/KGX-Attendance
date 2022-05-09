import requests
import json

rfid = input()
url = "https://intent-sunbeam-40.hasura.app/v1/graphql"
 
headers = {"Content-Type": "application/json; charset=utf-8", "x-hasura-admin-secret" : "4E9fBl6pQoyEL138Ov9jmoY3xnKtMpKm2KtrHWHPOUdcXzMHBzvII9CDooZZH5Ay"}

data = {
    "rfid_key": rfid,
}

response = requests.post(url, headers=headers, json=data)
 
print("Status Code", response.status_code)
print("JSON Response ", response.json())


