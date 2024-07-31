#Exception Handling: It allows smooth process of program execution even if an exception occurs.
#try : Run this code
#except: Execute this code when there is an exception
#else: No exceptions? Run this code
#finally: always run this code
#raise : We can use raise to throw an exception if a condition occurs
#assert: Tests if a condition is true, if it's false, program halts execution otherwise continue

import sys
'''
x =10
if x > 5:
    raise Exception("Number should increase by 5. The value of x was {}.".format(x))
'''

def linux_interaction():
    assert('linux' in sys.platform), "This code runs in linux only."
    print('do something')

'''
try:
    linux_interaction()
except:
    print('Linux function was not executed.')
'''

'''
try:
    linux_interaction()
    with open('file.txt') as f: #using alias
        read_data = f.read()
except FileNotFoundError as notfounderror: #using alias
    print(notfounderror)
except AssertionError as error: #using alias
    print(error)
    print('Linux function was not executed.')
'''

try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file1.txt') as f:
            read_f = f.read()
    except FileNotFoundError as notfoundfile:
        print(notfoundfile)
finally:
    print('Cleaning up, irrespective of any exceptions.')
