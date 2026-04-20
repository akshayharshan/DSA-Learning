# def fibanacci_number(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     sum = fibanacci_number(n-1) + fibanacci_number(n-2)
#     return sum
    
# print(fibanacci_number(5))


# def fibanacci_number(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     prev1 = 0
#     prev2 = 1
#     arr = [prev1,prev2]
#     for n in range(2,n):
#         temp = prev1 + prev2
#         prev1 = prev2
#         prev2 = temp
#         arr.append(temp)

#     return arr
        
    
# print(fibanacci_number(5))


# def prime_num(num):
#     if num < 2:
#         return False
#     arr = []
#     for i in range(2,num):
#         prime = True
#         for j in range(2,int(i ** 0.5)+1):
#             if i % j == 0:
#                 prime = False
#                 break
#         if prime:
#             arr.append(i)
#     return arr


# print(prime_num(10))



# def prime_num(num):
#     if num < 2:
#         return False

#     for i in range(2,num):
#         if num % i != 0:
#             return False
        

# print(prime_num(19))



# def reverse_num(num):
#     new_num = 0

#     while num > 0:
#         reminder = num % 10 
#         num = num // 10
#         new_num = new_num * 10 + reminder
#         num 
#     return new_num

# print(reverse_num(1234))


# def palindrome(num):
#     pal_num = num
#     reverse_num = 0

#     while pal_num > 0:
        
#         remainder = pal_num % 10
#         pal_num = pal_num // 10
#         reverse_num = reverse_num * 10 + remainder
#     return reverse_num == num

# print(palindrome(120)) # Output: True



def anagram(s,anagram):
    if len(s) != len(anagram):
        return False
    hashmap = {}
    for i in range(len(s)):
        hashmap[s[i]] = hashmap.get(s[i],0) + 1
    
    for char in anagram:
        if char not in hashmap or hashmap[char] == 0:
            return False
        hashmap[char] -=1
    return True





print(anagram("listen","silent"))


