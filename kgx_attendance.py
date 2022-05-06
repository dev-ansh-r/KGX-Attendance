import requests
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Kolkata') 
datetime = datetime.now(tz)
intime = datetime.strftime("%H:%M:%S")
createdat = datetime.strftime("%H:%M:%S")
updatedat = datetime.strftime("%H:%M:%S")

rfid_key = str(input(""))

payload = {"rfid_key" : rfid_key , "in_time" : intime , "created_at" : createdat , "updated_at" : updatedat}

print(payload)

###r = requests.post("", data = payload)



