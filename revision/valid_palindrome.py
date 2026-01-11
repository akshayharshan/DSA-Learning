def is_palindrome(s):
    s =  s.lower()
    l,r=0,len(s)-1
    while l < r:
        if not s[l].isalnum():
           l +=1
        elif not s[r].isalnum():
           r -=1
        elif s[l] != s[r]:
            return False
        else:
            l+=1
            r-=1
    else:
     return True

print(is_palindrome('A man, a plan, a canal: Panama'))

# for avoiding the special character we can use if not s[r].isalnum()/s[l].isalnum if not up each index
