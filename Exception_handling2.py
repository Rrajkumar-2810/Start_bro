x = input("Enter a number: ")
y = input("Enter a number: ")

try:
    z = int(x)/ int(y)
except Exception as e:
    z = None
    print("Exception of z:", e)
try:
    a = x / int(y)
except Exception as e:
    a = None
    print("Exception of a:",type(e).__name__)
print("Division of z:",z)
print("Division of a:",a)
