from datetime import datetime

a = datetime(2012,2,14,1,0,0)
b = datetime(2012,3,14,0,0,0)
print(a)

#difference between two dates

x = b - a
print(x)

#print(a.strftime("%Y-%m-%d %H:%M:%S"))

now = datetime.now()
print(now)


#string to date

strDate = "2012-02-14 01:00:00"
date = datetime.strptime(strDate, "%Y-%m-%d %H:%M:%S")
print(date.year)