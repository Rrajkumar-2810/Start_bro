#   List  = [] ordered and changeable. Duplicates OK

fruits = ["apple","orange","banana","coconut","watermelon"]

#print(fruits) # Prints as a list
#print(fruits[5:0:-1]) # Prints in reverse order

for x in fruits:
    print(x)  # Prints every element in a newline
print() # Just to show separation

for y in fruits:
    print(y, end=" ") # Prints every element with spaces in the same line
print() # Just to show separation

print("apple" in fruits) # Gives a boolean value depending on the value is present or not in the variable
print("mango" in fruits) # Gives a boolean value depending on the value is present or not in the variable

fruits[0] = "pineapple"
print(fruits) # Lists are mutable
fruits.append("mango") # You can add elements
print(fruits) 
fruits.remove("mango") # You can remove elements
print(fruits) 
fruits.insert(3,"guava") # You can insert elements at specific positions
print(fruits)
fruits.sort() # Sort the list elements alphabetically
print(fruits)
fruits.reverse() # Sort the list elements in reverse order
print(fruits)
print(fruits.clear) # clears all the elements and gives an empty list
