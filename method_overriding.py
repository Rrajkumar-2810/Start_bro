#method_overriding: It can be achieved to change functionality of parent class function.

class parent:
    def func1(self):
        print("This is function 1")

class child(parent):
    def func1(self):
        print("this is function 2")

ob = child()
ob.func1() # The parent class func1 is overridden with child class func1.
