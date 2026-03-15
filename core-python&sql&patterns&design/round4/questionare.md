def deco(func):
    def wrap(*args, **kwargs):
        print("Start")
        return func(*args, **kwargs)
    return wrap


@deco
def add(a, b):
    return a + b

print(add(2,3))

Q1)start
5
Q2) it actually open the file and read and exit which is for context manager __ENTER__, __EXIT__ are the methods 
