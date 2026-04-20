1) list is mutable can have dulpicates can be used to store integrers, strings etc but tuple is immutable and can have duplicates we can use it where we dont have to change after the creation and it is bit fater in performance wise

2)immutable objects canbe chnaged after the creation but mutable can be chnaged after the creation

3)generator is a function that is used to return value through yield , that means it takes values one by one rather than loading full into the memory this can be used for db instance

4) decorator is a function that is used for extend anotehr fucntion without changing the code of nthat fucntion explicitly

5) Encapsulation. ---> encapsulation avoid some class attributes to to acceced outside the clas socpe with _ and __  whuch is private and protected 

    class BankAccount:
        def __init__(self,balance):
            self.__balance = balance
        def deposit(self , amount):
            self.__balance ++ amount

    bank_acc = BankAccount(100)
    bank_acc.deposit(20)

    Inheritance -- > inheritance is parent child relationship where the child class will inherit from the parent so that the child class can access the methods from the parent class

        class Parent:

            def __init__(self,name):
                self.name = name
            def print_name(self):
                return str(self.name)

        class child(Parent):
            test = Parent("akshay")
            print(test.print_name)

    Polymorphism  ---> same method name but two different task is called ploymorphsm
        class Dog:
            def make_sound(self):
                return "bowww"

        class Cat:
            def make_sound(self):
                return "meowww"

        
        dog = Dog

        dog.make_sound()

        cat = Cat
        cat.make_sound()

    abstraction : this is where we have to hide the complex business logic and make sure the it is implemented in the class which uses abstarction


    6) dont know

    7) append to set and if a value in the set again return true that the duplicate exist

    8)O(n^2)




