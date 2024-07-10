#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates

fruits = {"apple","orange","banana","coconut","watermelon","orange"}
print(fruits) # Order of elements keeps changing

for x in fruits:
    print(x)
print()

#print(fruits[0]) # This will throw an error because it is unordered
fruits.add("Lichi")
print(fruits)
fruits.remove("apple")
print(fruits)

fruits.clear() # clears all the elements and gives an empty set
print(fruits) 