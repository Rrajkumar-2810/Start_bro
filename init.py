#__init__() : this function is called automatically everytime the class is used to create an object

class Parent:
    def __init__(self, fname, fage):
        self.name= fname
        self.age= fage

    def view(self):
        print(self.name, self.age)

class Child(Parent):
    def __init__(self, fname, fage):
        Parent.__init__(self, fname, fage)
        self.lastname="Kumar"

    def view(self):
        print(self.age, self.lastname, self.name)

ob = Child(23, 'Rishiraj')
ob.view()
