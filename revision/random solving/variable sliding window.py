s = "abcabcbb"
l=0
max_len = 0
seen = set()

for r in range(len(s)):
    while s[r] in seen:
        seen.remove(s[l])
        l+=1
        
    seen.add(s[r])
    max_len = max(len(seen),r-l+1)

print(max_len)

