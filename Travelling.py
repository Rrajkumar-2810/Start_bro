travelling = input("Are you travelling(Enter 'y' for yes and 'n' for no)?: ")
num_count = 0
while travelling == 'y':
    num = int(input("Number of people travelling?: "))
    for i in range(1, num+1):
        num_count=num_count +1
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        sex = input("Enter your gender(Male or Female): ")
        print(f"Name:",name)
        print(f"Age:",age)
        print(f"Sex:",sex)
    travelling = input("Did you forget someone?: ")
while travelling != 'y':
    print(f"Number of people travelling is {num_count}.")
    break
