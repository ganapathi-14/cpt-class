from datetime import datetime, date, timedelta

# current time and date
now = datetime.now()
print("Current DateTime :", now)
#only date
print("Today date : ",date.today())

#formatted datetime

formatted=now.strftime("%d-%m-%Y %H:%M:%S")
print(formatted)


formatted=now.strftime("%d-%m-%y %H:%M:%S")
print(formatted)

date_str="30-06-2025 11:52:43"
parsed=datetime.strptime(date_str,"%d-%m-%Y %H:%M:%S")
print("Parsed data : ",parsed)

#timedelta
tommorow=now+timedelta(days=1)
print("Tommorow : ",tommorow)
yesterday=now-timedelta(days=1)
print("Yesterday : ",yesterday)

#futureTime
ftime=now+timedelta(hours=3,minutes=30)
print("After 3.5 hours : ",ftime)

#fomat and am/pm
now = datetime.now()
format_12hr = now.strftime("%d/%m/%Y %I:%M:%S %p")
print(format_12hr)


# %I=0-12 hours
# %p=AM/PM
# %H - 0-23:59:59.00000
#mon,tue
#monday,tuesday

