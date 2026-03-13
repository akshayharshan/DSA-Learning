Python Interview Preparation – Day 3 (Advanced Python)
======================================================

Topics Covered
--------------

- Iterators
- Generators
- Decorators
- *args and **kwargs
- Context Managers

1. Iterators
------------

An iterator is an object that allows sequential access to elements one at a time.

Python provides two main functions:

| Function | Purpose                 |
|---------|-------------------------|
| iter()  | creates an iterator     |
| next()  | retrieves the next element |

**Example**

```python
numbers = [1,2,3]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))
```

**Output**

```python
1
2
3
```

If `next()` is called after the last element:

```python
StopIteration
```

2. Generators
-------------

Generators are functions that produce values lazily using `yield`.

They generate values on demand rather than storing all values in memory.

**Example**

```python
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1


for num in count_up(3):
    print(num)
```

**Output**

```python
1
2
3
```

**Key Advantage**

Generators are memory efficient because they generate values when needed.

3. Generator vs List
--------------------

**Example:**

List comprehension:

```python
[x*x for x in range(5)]
```

Generator expression:

```python
(x*x for x in range(5))
```

**Differences**

| List                         | Generator             |
|------------------------------|-----------------------|
| Stores all values in memory  | Produces values lazily |
| Uses more memory             | Memory efficient      |

4. Decorators
-------------

A decorator modifies or extends the behavior of a function without changing its code.

**Example**

```python
def deco(func):
    def wrap():
        print("Before")
        func()
        print("After")
    return wrap


@deco
def greet():
    print("Hello")

greet()
```

**Output**

```python
Before
Hello
After
```

**How Decorators Work**

Python converts:

```python
@deco
def greet():
    print("Hello")
```

into:

```python
def greet():
    print("Hello")

greet = deco(greet)
```

The decorator replaces the original function with the wrapper function.

5. Decorators with Arguments
----------------------------

If the wrapped function takes parameters, the wrapper must support them.

Use:

- `*args`
- `**kwargs`

**Example**

```python
def deco(func):
    def wrap(*args, **kwargs):
        print("Decorating")
        return func(*args, **kwargs)
    return wrap


@deco
def multiply(a, b):
    return a * b

print(multiply(3,4))
```

**Output**

```python
Decorating
12
```

6. *args and **kwargs
---------------------

**\*args**

Collects positional arguments into a tuple.

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

**\*\*kwargs**

Collects keyword arguments into a dictionary.

**Example:**

```python
def func(**kwargs):
    print(kwargs)

func(name="Akshay", age=25)
```

**Output:**

```python
{'name':'Akshay', 'age':25}
```

**Why Decorators Use Them**

Decorators do not know what parameters the wrapped function expects.

Using:

```python
*args, **kwargs
```

allows the decorator to work with any function signature.

7. Context Managers
-------------------

Context managers manage resources using the `with` statement.

**Example:**

```python
with open("file.txt") as f:
    data = f.read()
```

The file automatically closes after the block.

**Context Manager Methods**

A context manager defines two special methods:

| Method     | Purpose                              |
|-----------|--------------------------------------|
| __enter__() | executed when entering the with block |
| __exit__()  | executed when leaving the block      |

**Example**

```python
class Demo:

    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")


with Demo():
    print("Inside")
```

**Output**

```python
Enter
Inside
Exit
```

**Execution Flow**

```python
with Demo():
   ↓
__enter__()
   ↓
Execute block
   ↓
__exit__()
```

Even if an error occurs, `__exit__()` still executes.

**Interview Explanation**

A context manager ensures proper setup and cleanup of resources using the `with` statement by implementing `__enter__` and `__exit__`.