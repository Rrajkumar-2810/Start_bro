number = int(input("Enter a number: "))
fact = 1

if number < 0:
    print("Number should be positive.")
elif number == 0:
    print(f"Factorial is {fact}")
else:
    for i in range(1, number+1, 1):
        fact = fact * i
    print(f"Factorial is {fact}")
