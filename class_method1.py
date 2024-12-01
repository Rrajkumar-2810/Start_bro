class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def work(self):
        if self.occupation == "Tennis":
            print(self.name,"is a tennis player.")
        elif self.occupation == "Director":
            print(self.name,"is a movie director.")

    def speak(self):
        print(self.name,"asks how are you doing?")

n = input("Enter your name: ")
o = input("Enter your occupation('Tennis or Director'): ")
Person = Human("Raj", "Director")
user = Human(n,o)
user.work()
user.speak()
Person.work()
Person.speak()
