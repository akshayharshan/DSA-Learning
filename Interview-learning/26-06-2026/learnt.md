# Python Revision Notes - Iterators & Generators
## Backend Interview Preparation

---

# Topics Covered

- Iterable
- Iterator
- `iter()`
- `next()`
- StopIteration
- Iterator State
- How `for` Loop Works Internally
- Generator
- `yield`
- Lazy Evaluation
- Generator State
- Generator Exhaustion
- Generator vs Normal Function

---

# 1. Iterable

## Definition

An **iterable** is an object that can produce an iterator using the `iter()` function.

Common Iterables

- List
- Tuple
- Set
- Dictionary
- String
- Range

Example

```python
nums = [1,2,3]
```

`nums` is **NOT** an iterator.

It is an **iterable**.

---

# 2. Iterator

## Definition

An **iterator** is an object that returns one element at a time while maintaining its current position.

It supports

```python
next(iterator)
```

Example

```python
nums = [1,2,3]

it = iter(nums)
```

Now

```python
next(it)
```

returns

```
1
```

Second call

```python
next(it)
```

returns

```
2
```

Third

```
3
```

Fourth

```
StopIteration
```

---

# Relationship

```
Iterable

↓

iter()

↓

Iterator

↓

next()

↓

One Value

↓

Next Value

↓

Next Value

↓

StopIteration
```

---

# 3. iter()

Purpose

Convert an iterable into an iterator.

Example

```python
nums = [1,2,3]

it = iter(nums)
```

Before

```
nums

↓

Iterable
```

After

```
nums

↓

iter()

↓

Iterator
```

---

# 4. next()

Purpose

Retrieve the next element from an iterator.

Example

```python
it = iter([1,2,3])

next(it)
```

Output

```
1
```

Calling `next()` repeatedly moves the iterator forward.

---

# 5. StopIteration

Raised when an iterator has no more elements.

Example

```python
nums = [1]

it = iter(nums)

next(it)
next(it)
```

Output

```
1

StopIteration
```

---

# 6. Iterator State

An iterator remembers

- Current position
- Local execution state

Example

```python
nums = [10,20,30]

it = iter(nums)
```

Initially

```
10
20
30
 ^
```

After

```python
next(it)
```

```
10
20
30
    ^
```

After

```python
next(it)
```

```
10
20
30
       ^
```

The iterator remembers where it stopped.

---

# 7. Multiple Iterators

Example

```python
nums = [1,2,3]

it1 = iter(nums)

it2 = iter(nums)
```

Important

Each iterator has its own independent state.

Example

```python
next(it1)
next(it1)
next(it2)
next(it1)
```

Output

```
1
2
1
3
```

Reason

Both iterators are created from the same iterable but maintain different positions.

---

# 8. How a for Loop Works

Python internally does approximately this

```python
it = iter(nums)

while True:

    try:
        item = next(it)
        print(item)

    except StopIteration:
        break
```

Every `for` loop creates a new iterator from the iterable.

---

# Example

```python
nums = [1,2,3]

for x in nums:
    print(x)

for y in nums:
    print(y)
```

Why does it print twice?

Because

```
Loop 1

↓

iter(nums)

↓

Iterator 1

------------------

Loop 2

↓

iter(nums)

↓

Iterator 2
```

Each loop gets a fresh iterator.

---

# Reusing the Same Iterator

Example

```python
nums = [1,2,3]

it = iter(nums)

for x in it:
    print(x)

for y in it:
    print(y)
```

Output

```
1
2
3
```

Second loop prints nothing.

Reason

The iterator is already exhausted.

---

# 9. Generator

## Definition

A generator is a special type of iterator created using the `yield` keyword.

Example

```python
def numbers():

    yield 1

    yield 2

    yield 3
```

Creating it

```python
g = numbers()
```

does **NOT** execute the function.

It only creates a generator object.

---

# Generator is an Iterator

```
Generator Function

↓

Generator Object

↓

Iterator

↓

next()
```

Therefore

```python
next(g)
```

works directly.

---

# 10. yield

Unlike `return`

`yield`

- Produces one value
- Pauses execution
- Saves current state
- Resumes later

Example

```python
def demo():

    print("A")
    yield 1

    print("B")
    yield 2
```

Execution

```python
g = demo()

next(g)
```

Output

```
A

1
```

Function pauses after

```python
yield 1
```

Next call

```python
next(g)
```

Output

```
B

2
```

Execution resumes from where it paused.

---

# 11. return vs yield

| return | yield |
|---------|--------|
| Ends function | Pauses function |
| One final value | Produces one value at a time |
| Function destroyed | Function state preserved |
| Cannot resume | Can resume |

---

# 12. Lazy Evaluation

Generators do not create values until requested.

Example

```python
def numbers():

    for i in range(1000000):
        yield i
```

Creating generator

```python
g = numbers()
```

Generated values

```
None
```

Nothing is generated yet.

Only

```python
next(g)
```

creates

```
0
```

Second

```python
next(g)
```

creates

```
1
```

This is called **Lazy Evaluation**.

---

# 13. Memory Efficiency

## Normal Function

```python
def numbers():

    result=[]

    for i in range(1000000):
        result.append(i)

    return result
```

Memory

```
0
1
2
3
...
999999
```

Everything exists in RAM simultaneously.

---

## Generator

```python
def numbers():

    for i in range(1000000):

        yield i
```

Memory

```
Generate

↓

Return

↓

Forget

↓

Generate Next
```

Only one value exists at a time.

---

# Important Clarification

Generator remembers

✅ Current execution line

✅ Local variables

✅ Current position

Generator DOES NOT remember

❌ Every previously generated value

If previous values are needed

YOU must store them.

Example

```python
values=[]

for x in generator:

    values.append(x)
```

Now the list stores them.

---

# 14. Generator Exhaustion

Example

```python
g = numbers()

for x in g:
    print(x)

for y in g:
    print(y)
```

Output

```
1
2
3
```

Second loop

```
Nothing
```

Reason

The generator is an iterator.

Once exhausted

It cannot restart.

---

# Restarting a Generator

Create a new one.

```python
g = numbers()

for x in g:
    print(x)

g = numbers()

for x in g:
    print(x)
```

Now it prints again because a fresh generator object is created.

---

# Real Backend Uses

Generators are commonly used for

- Reading huge log files
- Reading CSV files line by line
- Streaming database records
- Streaming HTTP responses
- Large file downloads
- ETL pipelines
- Kafka consumers
- Background processing

---

# Interview Questions

## What is an Iterable?

An iterable is an object that can produce an iterator using the `iter()` function.

---

## What is an Iterator?

An iterator is an object that returns one element at a time using `next()` while maintaining its current position.

---

## What is a Generator?

A generator is a special type of iterator created using the `yield` keyword that lazily produces values one at a time while preserving its execution state.

---

## Difference Between Iterable and Iterator

| Iterable | Iterator |
|------------|------------|
| Can create iterator | Produces values |
| Uses `iter()` | Uses `next()` |
| No current state | Maintains current state |
| Can create multiple iterators | Gets exhausted |

---

## Difference Between return and yield

| return | yield |
|---------|--------|
| Ends execution | Pauses execution |
| Returns once | Produces multiple values |
| Cannot continue | Can resume |
| Creates all data before returning | Generates values on demand |

---

## Why are Generators Memory Efficient?

Because they generate values only when requested instead of storing all values in memory at once.

---

# Interview Cheat Sheet

```
Iterable
↓

iter()

↓

Iterator
↓

next()

↓

StopIteration

-------------------------

Generator

↓

Special Iterator

↓

yield

↓

Pause

↓

Resume

↓

Lazy Evaluation

↓

Memory Efficient
```

---

# Key Takeaways

- Every `for` loop creates an iterator internally.
- Iterators maintain state and become exhausted.
- A generator is a special kind of iterator.
- `yield` pauses execution instead of ending it.
- Generators generate values lazily.
- Generators remember their execution state, not previously generated values.
- If previous values are needed, your program must store them.
- Generators are ideal for processing large datasets efficiently.