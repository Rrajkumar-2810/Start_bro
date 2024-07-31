#super : this function directly calls the parent class method

class parent:
    def func1(self):
        print("This is function 1")

class child(parent):
    def func2(self):
        super().func1()
        print("this is function 2")

ob = child()
ob.func2()
