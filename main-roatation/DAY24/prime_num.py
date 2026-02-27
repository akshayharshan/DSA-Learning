def check_prime(num):

    if num > 1:
        if num == 2:
            return True
        for n in range(2,int(num**0.5)+1):
            if num % n == 0:
                return False
        return True
    else:
        return False
        





print(check_prime(21))