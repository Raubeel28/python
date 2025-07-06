import datetime

#date=datetime.date(2025,1,2)
date=datetime.date.today()
print(date)

#time=datetime.time(5,3,5)
time=datetime.datetime.now()
time=time.strftime("%H:%M:%S  %d-%m-%Y")
print(time)

target_datetime= datetime.datetime(2025,7,8,11,3,5)
current_datetime=datetime.datetime.now()

if target_datetime>current_datetime:
    print("This time is yet to come")
else:
    print("This time has passed ")