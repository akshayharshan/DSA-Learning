def recursive_sum(digit):
    if digit == 0:
        return 0
    
    return digit % 10 + (recursive_sum(digit // 10)) 




print(recursive_sum(1234))