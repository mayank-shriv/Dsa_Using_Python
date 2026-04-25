class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):  #Inheriting Animal
    def bark(self):
        print(self.name, "bark")


d = Dog("Tommy")
d.speak()
d.bark()
