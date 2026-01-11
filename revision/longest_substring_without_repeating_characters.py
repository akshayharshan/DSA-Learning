s = "pwwkew"
l=0
max_len = 0
seen = set()

for r in range(len(s)):
    # here when look into the s and check in the seen whether the element in the s is there in seen if yes then remove it not the new find in the loop r but the old one which is found in the left that is s[l]
    while s[r] in seen:  
        seen.remove(s[l])
        l+=1
    else:
        seen.add(s[r])
    print(seen)
    max_len = max(r-l+1,max_len)

print(max_len)
    
    
    

