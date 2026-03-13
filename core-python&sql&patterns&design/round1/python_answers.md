Python Interview Preparation Notes – Day 1
=========================================

1. Mutable Default Arguments
----------------------------

**Problem**

```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))
print(add_item(2))
```

**Output**

```python
[1]
[1,2]
```

**Reason**

Default arguments in Python are evaluated once at function definition time, not every time the function is called.

So the same list object is reused across function calls.

**Correct Fix**

```python
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

This ensures a new list is created for each call.

2. is vs ==
-----------

**Example:**

```python
a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)
```

**Output**

```python
True
False
```

**Explanation**

| Operator | Meaning                |
|---------|------------------------|
| ==      | compares values        |
| is      | compares memory identity |

So:

```python
a == b  # values equal
a is b  # different objects
```

3. Reference vs Reassignment
----------------------------

**Example:**

```python
a = [1,2,3]
b = a
a = [4,5,6]

print(b)
```

**Output**

```python
[1,2,3]
```

**Explanation**

Initially:

```python
a → [1,2,3]
b → same object
```

After reassignment:

```python
a → [4,5,6]
b → still points to old list
```

Reassignment changes the variable reference, not the original object.

4. List vs Tuple
----------------

**When to Use Tuple**

- Data should not change (immutability)
- Slightly better performance
- Can be used as dictionary keys

**Example:**

```python
d = {(1,2): "value"}
```

Lists cannot be dictionary keys because they are mutable.

5. *args and **kwargs
---------------------

**\*args**

Allows passing multiple positional arguments.

**Example:**

```python
def func(*args):
    print(args)

func(1,2,3)
```

**Output:**

```python
(1,2,3)
```

Inside the function, args is a tuple.

**\*\*kwargs**

Allows passing multiple keyword arguments.

**Example:**

```python
def func(**kwargs):
    print(kwargs)

func(name="Akshay", age=25)
```

**Output:**

```python
{'name':'Akshay','age':25}
```

kwargs is a dictionary.

**Combined Example**

```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1,2,3,name="Akshay")
```

**Output:**

```python
(1,2,3)
{'name':'Akshay'}
```

6. List Copying
---------------

**Copy using slicing**

```python
a = [1,2,3]
b = a[:]
```

This creates a shallow copy.

**Example:**

```python
a.append(4)
print(b)
```

**Output:**

```python
[1,2,3]
```

Because b is a different list.

7. Shallow Copy vs Deep Copy
----------------------------

**Example:**

```python
import copy

a = [[1,2],[3,4]]
b = copy.copy(a)
c = copy.deepcopy(a)

a[0][0] = 100

print(b)
print(c)
```

**Output**

```python
[[100,2],[3,4]]
[[1,2],[3,4]]
```

**Explanation**

| Copy Type   | Behavior                  |
|------------|---------------------------|
| Shallow copy | copies outer container  |
| Deep copy    | copies everything recursively |

8. Mutation vs Reassignment
---------------------------

**Example 1 – Mutation**

```python
a = [1,2,3]
b = a
a.append(4)

print(b)
```

**Output:**

```python
[1,2,3,4]
```

Because the same list object was modified.

**Example 2 – Reassignment**

```python
a = [1,2,3]
b = a
b = b + [4]

print(a)
```

**Output:**

```python
[1,2,3]
```

Because b + [4] creates a new list object.

9. Shallow Copy with Nested Lists
---------------------------------

**Example:**

```python
a = [[1,2],[3,4]]
b = a.copy()

a[0] = [100,200]

print(b)
```

**Output:**

```python
[[1,2],[3,4]]
```

**Explanation**

This reassigns the outer reference, not the shared inner object.

If we mutated instead:

```python
a[0][0] = 100
```

Then both lists would change.