name = "Bro"
age = 45
gpa =4.5
student =True

print("Before conversion:",name) #Bro
print(type(name)) #<class 'str'>
age = int(age)
print(type(name)) #<class 'str'>
print("After Conversion:",name) #Bro

print("Before conversion:",age) #45
print(type(age)) #<class 'int'>
age = float(age) 
print(type(age)) #<class 'float'>
print("After Conversion:",age) #45.0

print("Before conversion:",gpa) #4.5
print(type(gpa)) #<class 'float'>
gpa = int(gpa)
print(type(gpa)) #<class 'int'>
print("After Conversion:",gpa) #4

student = str(student) 
print(student) #True
print(type(student)) #<class 'str'>

age = bool(age)
print("Age=",age) #Age= True
print(bool(0)) #False
print(bool(-1000)) #True
print(bool(100000)) #True

name = bool(name)
print(name) #True
print(bool(" ")) #True

x=2
y=2.0
x = x/y
print("The value of the variable changed from a int to a float=",x)
