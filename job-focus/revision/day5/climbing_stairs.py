def climbing_stairs(n):
    if n <= 0 :
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    prev1 = 1
    prev2 = 2
    for _ in range(3,n+1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr
    return prev2


print(climbing_stairs(6))