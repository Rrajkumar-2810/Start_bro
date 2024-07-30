#Creation of arrays
#Three ways of importing array in python are:
#1. Without alias: import array
#2. Using alias: import array as arr
#3. Using *: from array import*

#1.
import array
a = array.array('i',[4,2,7,9,8])
print(a)

#2.
import array as arr
a1 = arr.array('i',[5,8,0,2,8,6])
print(a1)

#3.
from array import*
a3 = array('i',[5,9,1,2,3,4])
print(a3)
