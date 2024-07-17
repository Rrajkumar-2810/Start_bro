#List vs numpy
#List array requires more memory
#Numpy array requires less memory
#List requires more time
#Numpy requires less time

#1. Memory
import numpy as np
import sys
import time

s= range(1000) 
print(f"Space required by the List array:",sys.getsizeof(100)*len(s)) #Doesn't matter what number is inside the getsize function

d= np.arange(1000)
print(f"Space required by the Numpy array:",d.size*d.itemsize)

#2. Time
size = 1000000

l1 = range(size)
l2 = range(size)

a1= np.arange(size)
a2= np.arange(size)

start = time.time()
result= [(x,y) for x,y in zip(l1,l2)] #Sum operation of two lists time taken
print(f"Time required by lists:",(time.time()-start)*1000)

start = time.time()
result= a1+a2
print(f"Time required by numpy:",(time.time()-start)*1000)
