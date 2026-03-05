def fibonacci(n):

    result = [1] * n
    for i in range(n):
        if i == 0:
            result[i] = 0
        elif i == 1:
            result[i] = 1
        else:
            result[i] = result[i-1] + result[i-2]
    return result

print(fibonacci(7))
