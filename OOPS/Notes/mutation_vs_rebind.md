# 🐍 Python Advanced Fundamentals
> A deep dive into Object Lifecycle, Memory References, and the Mechanics of Decorators.

---

## 📑 Table of Contents
1. [Mutation vs. Rebinding](#1-mutation-vs-rebinding)
2. [Shallow Copy Mechanics](#2-shallow-copy-mechanics)
3. [The Anatomy of a Decorator](#3-the-anatomy-of-a-decorator)
4. [Production-Ready Patterns](#4-production-ready-patterns)
5. [The Power of @wraps](#5-the-power-of-wraps)
6. [Execution Timing & Lifecycle](#6-execution-timing--lifecycle)

---

## 1️⃣ Mutation vs. Rebinding

Understanding the difference between changing an **object** and changing a **reference** is vital for bug-free code.

### **Mutation**
*Changing the object’s internal state.*
```python
a = [1, 2]
a.append(3)


Object ID: Does NOT change.

Content: Changes in place.

Side Effects: All references to this object see the update.

Rebinding
Changing what a variable points to.


a = [1, 2]
a = [3, 4]

Object ID: Variable now points to a new object.

Old Object: Unaffected (and eventually garbage collected).

Golden Rule: Mutation changes the object. Rebinding changes the reference.


Shallow Copy Mechanics
A shallow copy creates a new outer container, but the nested elements remain shared references.

a = [[1], [2]]
b = a.copy()

Action,Code,Result
Mutate Inner,a[0].append(3),Both a and b change (Shared reference).
Rebind Index,a[0] = [9],Only a changes (Reference replaced).

3️⃣ The Anatomy of a Decorator

A decorator is fundamentally syntactic sugar for rebinding a function name to a wrapper.

@outer
def greet():
    pass
Under the hood:
greet = outer(greet)
The variable greet is rebound to the function returned by outer.

4️⃣ Production-Ready Patterns

Basic Template
A simple closure that wraps a function (no argument support).

def outer(func):
    def inner():
        print("Before")
        func()
        print("After")
    return inner

Standard Template (Universal)
Using *args and **kwargs allows the decorator to work on any function.

from functools import wraps

def outer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("Log: Before Execution")
        result = func(*args, **kwargs)
        print("Log: After Execution")
        return result
    return inner


5️⃣ The Power of @wraps
Metadata preservation is key for debugging, IDE autocomplete, and documentation.

Without @wraps: greet.__name__ → "inner" (The wrapper hides the identity).

With @wraps: greet.__name__ → "greet" (Identity is preserved).



6️⃣ Execution Timing & Lifecycle
Important: Decorators execute at Definition Time, not Call Time.

@outer
def greet():
    print("Hello!")

Definition (Load Time): outer(greet) runs immediately when the module is imported or run.

Call (Runtime): Only the code inside the inner function runs when you actually invoke greet().