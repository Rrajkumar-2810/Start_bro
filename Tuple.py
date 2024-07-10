#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER


fruits = ("apple","orange","banana","coconut","watermelon","orange")
print(fruits) # Order of elements keeps changing

for x in fruits:
    print(x)
print()

print(fruits.index("coconut")) # Specifies the index position
print(fruits.count("orange")) # Counts the number of elemnts

# Can add, insert, pop or remove elements from the List
