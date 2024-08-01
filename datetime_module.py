#datetime() : datetime constructor.
#datetime.today(): returns the current date and time.
#datetime.now(): returns the current date and time.
#date(): Takes year, month and day as parameter and creates the corresponding date.
#time(): Takes hour, minutes, seconds, microseconds and tzinfo as parameter and creates the corresponding date.
#datetime.fromstamp(): converts seconds to return the corresponding date and time
#timedelta(): It is the difference between different dates or times

import datetime
a = datetime.datetime(2019,6,21,4,24,47,754)
print(a)

#print(datetime.datetime.today())
#print(datetime.datetime.now())

v=datetime.datetime.today()
print(v.year)
print(v.month)
print(v.day)
print(v.hour)

b1= datetime.timedelta(days=30)
b2= datetime.timedelta(days=20)
b3 = b1-b2
print(b3)
print(type(b3))
