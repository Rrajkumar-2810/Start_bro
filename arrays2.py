#Basic Array OPerations:-

#1.Finding length of an array: len()

#2.Adding/Changing length of an array : functions used:- 1.append() 2.extend() 3.insert()
#append() : When you want to add one element at the end of an array
#extend() : When you want to add more than one element at the end of an array
#insert() : when you want to add an element at a specific position in an array 

#3.Removing/Deleting length of an array : functions used:- 1.pop() 2.remove()
#pop() : Used when you want to remove an element and return it.
#remove() : Used when you want to remove an element with a specific value without returning it.

#4.Array Concatenation : using '+' symbol

#5.Slicing : variable[start_position: end_position]

#6.Looping through an array : Loops:- 1.for 2.while

#1
from array import*
a= array('i',[8,4,6,3,1])
print(len(a)) 
print('Original array:',a)

#2.1 appended
a.append(5)
print('Appended Array:',a)

#2.2 extended
a.extend([2,7]) 
print('Extended array:',a)

#2.3 inserted
a.insert(0,9)
print('Inserted Array:',a)

#3
b= array('i', [6,3,4,8,9,2,7])
print('Popping the last element:',b.pop())
print('Popping the first element:',b.pop(0)) #index position
print('Removing a specific value:',b.remove(8)) #value 
print(b)

#4
c = array('i')
c=a+b
print('Concatenated array:',c)

#5
print('Slicing array c:',c[0:4])
print(c[0:-2])

#6.1
d = array('i',[8,4,6,3,1,5,2,7,0,9])
for x in d:
    print((x), end =' ')
print()

#6.2
e = array('i', [6,3,4,8,9,2,7])
f=0
while f<len(e):
    print(e[f])
    f=f+1
