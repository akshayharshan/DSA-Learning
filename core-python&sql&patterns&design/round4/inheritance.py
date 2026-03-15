class Animal:
    def speak(self):
        print("Animal sound")
class Dog(Animal):

    def bark(self):
        print("Dog barking")

d = Dog()

d.speak()