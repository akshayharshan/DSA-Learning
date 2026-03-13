def climb_stairs(n):
    if n <=2:
        return n
    prev1 = 1
    prev2 = 2
    for i in range(3,n+1):

        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr
    return prev2 

# print(climb_stairs(7))

# climbing staires starts from 1 and continue that is why we dont choose prev1 = 1 and prev 2 =2

# but real fibancci is 0,1,1,2,3,5,8,....

def fibanacci(n):
    if n <=1:
        return n
    prev1 = 0
    prev2 = 1
    for i in range(2,n+1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr
    return prev2
print(fibanacci(7))


        