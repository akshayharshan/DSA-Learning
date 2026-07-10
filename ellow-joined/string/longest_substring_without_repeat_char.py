def longest_repeat_char(s):
    seen = set()
    l = 0
    max_size = 0
    for r  in range(len(s)):
        
        while s[r] in seen:
            seen.remove(s[l])
            l+=1
        else:
            seen.add(s[r])
        max_size = max(max_size,r-l+1)

    return max_size
s = "xyzzabcd"
print(longest_repeat_char(s))