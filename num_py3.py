import numpy as np

a= np.array([(3,2,1),(6,5,4)])
print(f"Convert into one single array:",np.ravel(a))
print(f"Column:",a.sum(axis=0))
print(f"Rows:",a.sum(axis=1))
print(f"Square root of every number:",np.sqrt(a))
print(f"Standard Deviation:",np.std(a))

b= np.array([(3,2,1),(6,5,4)])
c= np.array([(3,2,1),(6,5,4)])
print(b+c) #Addition
print(b-c) #Subtraction
print(b*c) #Multiplication
print(b/c) #Division
print(f"Horizontal Stacking:",np.hstack((b,c)))
print(f"Vertical Stacking:",np.vstack((b,c)))
