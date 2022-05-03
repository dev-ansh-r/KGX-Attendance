from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Kolkata') 
datetime = datetime.now(tz)
time_in = datetime.strftime("%H:%M:%S")

while(True):
  tagid = input()
  if tagid == "0009288976":
    print("name : Devansh Shukla","IN_Time : ",time_in)
  elif tagid == "0009208703":
    print("name : NawinRaj Kumar","IN_Time :",time_in)
  elif tagid == "0008865576":
    print("name : Bhuvaneshwari K","IN_Time : ",time_in)
  elif tagid == "0005513200":
    print("name : Sathasivam T","IN_Time : ",time_in)
  elif tagid == "0009293482":
    print("name : Roshan J","IN_Time : ",time_in)
  elif tagid == "0009289037":
    print("name : Kubera Prijesh D","IN_Time : ",time_in)  