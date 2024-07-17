import numpy as np

a = np.array([(1,2,3,4),(5,6,7,8)])
print(f"Original array:",a)
print(f"3rd element:",a[0:,3]) #Prints all the 3rd elements of all the rows present in the array

a = a.reshape(4,2)
print(f"Reshaped array:",a)

b = np.array([(9,8,7,6),(1,3,5,4),(14,10,12,11)])
print(f"3rd element:",b[0:,3]) #Prints all the 3rd elements of all the rows present in the array
print(f"3rd element:",b[0:2,3]) #Prints all the 3rd elements of all the rows present in the array upto 2nd row

c= np.linspace(1,5,4) #Gives number of values equally spaced between initial and final values(start, end, number of values equally spaced)
print(c)

d = np.array([(2,5,7,3)])
print(f"Max_d:",d.max())
print(f"Min_d:",d.min())
print(f"Sum_d:",d.sum())

print(f"Max_a:",a.max())
print(f"Min_a:",a.min())
print(f"Sum_a:",a.sum())

print(f"Max_b:",b.max())
print(f"Min_b:",b.min())
print(f"Sum_b:",b.sum())