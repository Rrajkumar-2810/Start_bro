#1 Username shouldn't contain more than 12 characters.
#2 Username shouldn't contain any spaces.
#3 USername shouldn't contain any numbers.

username= input("Enter a username: ")

if len(username) > 12 :
    print("Username shouldn't be greater than 12 characters.")
elif not username.find(" ") == -1:
    print("Username shouldn't contain any spaces.")
elif not username.isalpha():
    print("Username shouldn't contain any numbers.")
else:
    print(f"Welcome aboard {username}")
