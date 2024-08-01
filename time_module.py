#Time module: BEgins recording time from epoch i.e., 00:00:00 from 1st Jan, 1970.
#time(): returns the numbert of seconds.
#ctime(): returns the current date and time.
#sleep(): stops execution of a thread for the given duration.
#localtime(): returns the date and time in time.struct_time format.
#gmtime(): returns time.struct_time in UTC format
#mktime(): returns the seconds passed since epoch has passed
#asctime(): returns the string representing the same

import time

print(time.time())
print(time.ctime(1722512996.7973797))

a = time.localtime()
print(a)

b = time.mktime(a)
print(b)

c = time.asctime(a)
print(c)

x = time.strftime("%m/%d/%Y")
print(x)

s = "01 August 2024"
g= time.strptime(s, "%d %B %Y")
print(g)
