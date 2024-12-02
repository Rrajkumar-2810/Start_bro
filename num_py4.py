import numpy as np

a = np.array([5,4,3])
print(a[0])
print(a.itemsize) #IntegerSize
print(a.dtype) #DataType
print("A's no. of elements=",a.size) #Number of elements within the array
print("A's dimension:",a.ndim) #Dimension
print("A's shape=", a.shape)
print("a=",a)

b = np.array([[4,2,1],[7,3,9],[6,5,0]])
print(b[1][0])
print("B's dimensional:",b.ndim) #Dimension
print("B's IntegerSize",b.itemsize) #IntegerSize
print("B's datatype=",b.dtype) #DataType
print("B's no.of elements=",b.size) #Number of elements within the array
print("B's shape=", b.shape)
print("b=",b)

b = np.array([[4,2,1],[7,3,9],[6,5,0]], dtype=np.float64)
print("B's IntegerSize",b.itemsize) #IntegerSize
print("B's datatype=",b.dtype) #DataType
print("b=",b)

c = np.array([[4,2,1],[7,3,9],[6,5,0]], dtype=complex)
print("c=", c)
print("C's dimension=",c.ndim)
print("C's shape=",c.shape)
print("C's no.of elements=",c.size)
