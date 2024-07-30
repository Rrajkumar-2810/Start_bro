#Lambda function is a small anonymous function. It can take any number of arguments, but can only have one function.
#The power of lambda is better known when we use them as anonymous function inside another function.
#It is also known as a nameless function.
#lambda is not a name, but it's a keyword.
#One-time use: knows as throw-away functions as it is needed only/just once
#They are also passed as I/O of other higher-order functions.
#The body of a lambda function is written in a single line.

x = lambda a: a+10
print('x=',x(5))

x1 = lambda a,b : (a+b)*(a-b)
print('x1=',x1(10, 5))

x2 = lambda a,b,c : (a*b*c)/(a+b+c)
print('x2=',x2(5,4,3))

def functest(n):
    return lambda a: (a+n)*(a-n)
ina = functest(5) #the value of n is stored here
ina1 = functest(10) #the value of n is stored here
print('ina=',ina(8)) #the value of a is stored here
print('ina1=',ina1(14)) #the value of a is stored here

def funtest1(n):
    return lambda a,b,c : (a*b*c)/(a+b+c)/n
ina2 = funtest1(2)
print('ina2=',ina2(4,8,3))
