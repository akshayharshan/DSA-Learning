def palindrome_number(num):
    reverse = 0
    real_num = num
    while num != 0:
        rem = num % 10
        reverse = reverse * 10 + rem
        num = num // 10
    return real_num == reverse 





print(palindrome_number(124))