# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))


def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)

    result = 0

    for num in num_str:
        result += int(num) ** power

    return result 






# Test
print(is_armstrong(153))   # True
print(is_armstrong(123))   # False