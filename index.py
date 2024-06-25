# Seeing the use cases of String Indexing

credit_number= "1234-8524-9564-2467"

print(credit_number[0]) #accessing 0th element
print(credit_number[:4]) #accessing 0th to 3rd element
print(credit_number[5:9]) #accesing 5th to 8th element
print(credit_number[5:]) #accessing 5th to last element of the string
print(credit_number[-1]) #accessing the last element of the string
print(credit_number[::2]) #accessing 0th to last element with step count 2
print(credit_number[::3]) #accessing 0th to last element with step count 3

last_4digits= credit_number[-4:]
print(last_4digits) #Printing the last 4 didgits
# another way of printing thw credit_number last four digits can be like this as well
print(f"XXXX-XXXX-XXXX-{last_4digits}")

#Printing the string in reverse
reverse_number = credit_number[::-1]
print(reverse_number)

