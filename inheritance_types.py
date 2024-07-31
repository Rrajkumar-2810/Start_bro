#Inheritance is of four types: 1.Single  2.Multiple  3.Multilevel  4.Heirarchical
#Single : When the inheritance involves one parent class and one child class.
#Multiple : When the inheritance involves more than one parent class.
#Multilevel : The child class acts as a parent class for another child class.
#Heirarchical : More than one type of Inheritance.

#2
print("Multiple Inheritance")
class Parent:
    def func1(self):
        print("this is function1")

class Parent1:
    def func3(self):
        print("This is function3")

class Child(Parent, Parent1):
    def func2(self):
        print("this is function2")
ob = Child()
ob.func1()
ob.func3()

#3
print("Multilevel Inheritance")
class Parent2:
    def func4(self):
        print("this is function4")

class Child1(Parent2):
    def func5(self):
        print("this is function5")

class Child2(Child1):
    def fun6(self):
        print("this is function6")

ob1 = Child2()
ob1.func4()
ob1.func5()

#4
print("Heirarchial Inheritance")
class Parent3:
    def func6(self):
        print("this is function6")

class Child3(Parent3):
    def func7(self):
        print("this is function7")

class Child4:
    def func8(self):
        print("this is function8")

class Child5(Parent3, Child4):
    def func9(self):
        print("this is function9")

ob2 = Child5()
ob2.func6()
ob2.func8()
