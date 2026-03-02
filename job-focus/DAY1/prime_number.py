def check_prime_num(num):
    if num <= 1:
        return False
    if num == 2 :
        return True
    for n in range(2,int(num ** 0.5)+ 1):
        if num % n == 0:
            return False
    return True





print(check_prime_num(49))