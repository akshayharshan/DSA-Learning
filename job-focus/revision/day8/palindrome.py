def palindrome(num):
    new_num = num
    reminder = 0
    number = 0
    while new_num  > 0:
        reminder = new_num % 10
        number =  number * 10 + reminder
        new_num = new_num // 10
        
    return number


print(palindrome(1331))