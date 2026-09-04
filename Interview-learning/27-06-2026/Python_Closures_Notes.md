# Python Closures - Interview Notes

## Definition

A closure is an inner function that remembers variables from its
enclosing function even after the enclosing function has returned.

## Example

``` python
def outer():
    x = 10

    def inner():
        print(x)

    return inner

f = outer()
f()
```

Output:

    10

## Why Doesn't x Disappear?

-   Normally, local variables are destroyed when a function returns.
-   Python notices that `inner()` still uses `x`.
-   Python stores only the required variables in a **closure**.
-   The outer stack frame is destroyed, but the closure survives.

## Memory Model

    outer() Stack
    -------------
    x = 10
    -------------

    return inner

    ↓

    Stack Destroyed

    ↓

    Inner Function
          │
          ▼
    Closure
    -------
    x = 10
    -------

## Closures in Decorators

``` python
def logger(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
```

`wrapper()` remembers `func` through a closure.

## Key Points

-   Captures outer variables.
-   Does not preserve the entire stack frame.
-   Preserves only referenced variables.
-   Makes decorators possible.

## Interview Answers

**What is a closure?**

A closure is a function that retains access to variables from its
enclosing scope even after the enclosing function has returned.

**How are closures used in decorators?**

The wrapper function stores the original function (`func`) in its
closure so it can call it later.

## Summary

-   Functions are first-class objects.
-   Functions can be passed and returned.
-   Closures remember outer variables.
-   Decorators are built on closures.
