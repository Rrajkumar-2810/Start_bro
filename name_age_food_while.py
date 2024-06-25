name= input("Enter a name: ")

while name =="":
    print("You did not enter your name: ")
    name=input("Please enter your name: ")

age = int(input("Enter your age: "))
while age <0:
    print("Age cannot be negative")
    age = int(input("Please enter your age: "))

food = input("Enter the name of the food you like(Enter q to quit): ")
while not food=='q':
    print("Oh! so this is your favourite {food}.")
    food = input("Enter another food you like(Enter q to quit): ")

print(f"Your name is: {name}")
print(f"Hello, {name}.")
print(f"Your age is {age} years.")
print("I am out")
