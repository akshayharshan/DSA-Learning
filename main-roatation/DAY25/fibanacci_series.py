def fibanacci_series(num):
   

    if num <= 0:
        return []
    if num == 1:
        return [0]
    arr =[0,1]
    for i in range(2,num):
        next_val = arr[i-1] + arr[i-2]
        arr.append(next_val)
    return arr


print(fibanacci_series(6))



def fib(num):
    if num == 0 :
        return 0
    if num == 1:
        return 1

    return fib(num-1) + fib(num-2)

print(fib(6))
