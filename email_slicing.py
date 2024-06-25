email= input("Enter a email: ")
# for example "heybuddy@example.com"
index = email.index('@')
username= email[:index] 
domain= email[index+1:]

#This is a more optimized approach to this problem
"""
username= email[: email.index('@')]
domain = email[email.index('@')+1 :]]
"""

print(f"Your username is {username} and domain is {domain}.")
