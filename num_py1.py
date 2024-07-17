import numpy as np

a = np.array([(3,9,6),(4,7,1),(5,2,8)])
print(f"The array:",a)
print(f"The Dimensions:",a.ndim)
print(f"Byte size:",a.itemsize)
print(f"Data type:",a.dtype)
print(f"Size:",a.size) # size of the array(Should be containing homozenous number of elements)
print(f"Shape:",a.shape) # shape of the array(rows, columns)

print(f"The exponential functions are:",np.exp(a))
print(f"The Logarithmic functions are:",np.log(a)) #Natural logarithm
print(f"The Logarithmic functions of log base 10 are:",np.log10(a)) #Base logarithm
