#Deleting a file

f = open('D:/vn/log4.txt', 'w')
f.write("This file is just created, it didn't existed before.\n")
f.write("You don't believe me, do you?")
f = open('D:/vn/log4.txt', 'r')
print(f.read())
f.close()

f = open('D:/vn/log4.txt', 'a')
f.write('\nThat is your choice whether to believe or not.')
f.write("\nI won't hold anything against ya.")
f = open('D:/vn/log4.txt', 'r')
print(f.read())
f.close()

import os
if os.path.exists('log4.txt'):
    os.remove('log4.txt')
else:
    print("File doesn't exist.")
