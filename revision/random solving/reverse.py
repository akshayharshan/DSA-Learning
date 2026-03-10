s= ["h","e","l","l","o"]
l =0
r = len(s)-1
while l < r:
    s[l],s[r] = s[r],s[l]
    print(s)
    l+=1
    r-=1
print(s)