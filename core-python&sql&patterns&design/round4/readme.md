OOP & Advanced Python – Round 4
===============================

---

1. Encapsulation
----------------

Encapsulation means restricting direct access to internal data and exposing it through methods.

**Example**

```python
class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance


acc = BankAccount(1000)
acc.deposit(500)

print(acc.get_balance())
```

**Output:**

```python
1500
```

**Interview Explanation**

Encapsulation bundles data and methods together and restricts direct access to internal state.

---

2. Inheritance
--------------

Inheritance allows a class to reuse functionality of another class.

**Example**

```python
class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def bark(self):
        print("Dog barking")


d = Dog()

d.speak()
d.bark()
```

**Output**

```python
Animal sound
Dog barking
```

**Interview Explanation**

Inheritance enables code reuse by allowing a class to inherit attributes and methods from another class.

---

3. Polymorphism
---------------

Polymorphism means same method name but different behavior.

**Example**

```python
class Dog:
    def speak(self):
        print("Bark")


class Cat:
    def speak(self):
        print("Meow")


animals = [Dog(), Cat()]

for a in animals:
    a.speak()
```

**Output**

```python
Bark
Meow
```

**Interview Explanation**

Polymorphism allows different objects to respond to the same method call in different ways.

---

4. Abstraction
--------------

Abstraction hides internal implementation details and exposes only necessary functionality.

**Example**

```python
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


s = Square(4)
print(s.area())
```

**Output**

```python
16
```

---

5. @classmethod vs @staticmethod
--------------------------------

**Example**

```python
class Example:

    value = 10

    @classmethod
    def cls_method(cls):
        print(cls.value)

    @staticmethod
    def static_method():
        print("Static method")


Example.cls_method()
Example.static_method()
```

**Output**

```python
10
Static method
```

**Differences**

| Feature               | classmethod      | staticmethod     |
|-----------------------|------------------|------------------|
| First parameter       | cls              | none             |
| Access class variables| Yes              | No               |
| Access instance variables | No          | No               |
| Use case              | class-level logic | utility function |

---

6. Composition vs Inheritance
-----------------------------

**Inheritance**

- Dog is an Animal

**Composition**

- Car has an Engine

**Composition Example**

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
```

---

7. Method Resolution Order (MRO)
--------------------------------

MRO defines the order Python searches classes when multiple inheritance is used.

**Example**

```python
class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(A):
    def show(self):
        print("C")


class D(B, C):
    pass


d = D()
d.show()
```

**Output**

```python
C
```

**MRO Order**

```python
D → B → C → A → object
```

You can check using:

```python
print(D.mro())
```