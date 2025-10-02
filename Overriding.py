class Animal:
    def show(self):
        print("hello i am Ajay")

class Human(Animal):
    def show(self):
        print("hello i am human")

obj = Human()
obj.show()  