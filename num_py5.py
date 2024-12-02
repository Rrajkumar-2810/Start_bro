import numpy as np

a= np.zeros( (4,2) ) #rows, columns
print(a)

b = np.ones( (3,2) )
print(b)

#array range
c = np.arange(1,5)
print("C=", c)

#generating numbers which are linearly spaced
d = np.linspace(2,5,10)
print(d)

#Reshaping the array
e = np.array([[4,2],[7,3],[6,5]])
print("E axis=0 sum=",e.sum(axis=0))
print("E axis=1 sum=",e.sum(axis=1))
print("e=", e.reshape(3,2))
print("E=",e)
print("e=", e.reshape(6,1))
print("E=",e)
print("e=", e.ravel()) #Raveling the array as 1D

print("E's max=",e.max())
print("E's min=",e.min())
print("E's sum=",e.sum())
print("E axis=0 sum=",e.sum(axis=0))
print("E axis=1 sum=",e.sum(axis=1))

print("Square root=",np.sqrt(e))
print("Standard Deviation=",np.std(e))
