#database 
from influxdb import InfluxDBClient
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Kolkata') 
datetime = datetime.now(tz)
time_in = datetime.strftime("%H:%M:%S")

#setup database
client = InfluxDBClient('localhost',8086,'admin','passphrase','kg-attendance')
client.create_datbase('Kg-attendance')
client.get_list_datbase()
client.switch_datbase('Kg-attendance')


while(True):
  tagid = input()
  if tagid == "0009288976":
    tagid1 = { "name" : "Devansh Shukla","IN_Time ": time_in }
  elif tagid == "0009208703":
    tagid1={"name" : "NawinRaj Kumar","IN_Time": time_in}
  elif tagid == "0008865576": 
    tagid1= {"name" : "Bhuvaneshwari K","IN_Time ": time_in}
  elif tagid == "0005513200":
    tagid1 = {'name' : 'Sathasivam T',"IN_Time " : time_in}
  elif tagid == "0009293482":
    tagid1 = {"name" : "Roshan J","IN_Time " : time_in }
  elif tagid == "0009289037":
    tagid1 = {"name" : " Kubera Prijesh D","IN_Time " : time_in}  

#setup payload
json_payload =[]
data = tagid1
json_payload.append(data)

#send our payload
client.write_points(json_payload)



