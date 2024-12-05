#Filter: Used to filter given iterables(lists, sets, etc) with the help of another function passed as an argument to test all the arguments to be true/false.
#Map: Applies a given function to all the iterables and returns a new list and gives result in the form of True/False.
#Reduce: Applies some function to a list that are passed as a parameter and returns only a single value.

list1 = [1,2,3,4,5,6,7,8,9]
file1 = list(filter(lambda x: x%2==0, list1))
print(file1)

file2 = list(map(lambda x: x%2==0, list1))
print(file2)

from functools import reduce
file3 = reduce(lambda a,b: a+b, list1)
print(file3)
