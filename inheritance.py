#When a child class inherit the property of parent class, it is called inheritance.
#uses: 1.Code Reusability 2.Transition and Readability 3.Real world Relationship

#Single Inheritance
class Parent:
    def func1(self):
        print("It is a parent class")

class child(Parent):
    def func2(self):
        print("It is a child class")

print("Accessing the parent through the help of a variable having access to the child class")
ob = child()
ob.func1()
ob.func2()
