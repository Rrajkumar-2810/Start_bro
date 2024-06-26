name = input("Enter your name: ")
age = int(input("Enter your age: "))
age =age+1
print(f"Hello {name}")
print(f"you are {age} years old")

item= input("What would you like to buy?:")
price= int(input("What is the price?: "))
quantity= int(input("How many would you like to buy?: "))

total = price * quantity
print(f"You have bought {quantity} * {item}/s")
print(f"Your total is: ${round(total,2)}")
