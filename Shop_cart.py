#Shooping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy(Enter q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("***** Your cart *****")

for food in foods:
    print(food, end=" ")
print()

for price in prices:
    total = total+price # total += price
    print(price, end =" ")
print()

print(f"Yout total is: ${total:0.2f}")
