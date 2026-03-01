def check_palindome_num(num):
    rev_num = num
    reverse = 0


    while rev_num > 0:
        rem = rev_num % 10
        reverse = reverse * 10 + rem
        rev_num =  rev_num // 10
    
    if reverse == num:
        return True
    else:
        return False




print(check_palindome_num(121))