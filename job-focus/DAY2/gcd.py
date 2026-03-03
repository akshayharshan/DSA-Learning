# def gcd(num1,num2):

#     while num2 != 0:
#         num1,num2 = num2,num1 % num2
#     return num1

# print(gcd(27,9))


def gcd(num1,num2):

    if num2 == 0:
        return num1
    else:
       return  gcd(num2,num1 % num2)

print(gcd(27,9))