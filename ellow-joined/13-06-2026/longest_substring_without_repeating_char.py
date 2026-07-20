def longest_substring(s):
    max_len = 0
    l = 0
    list = []
    for r in range(len(s)):
        
        while s[r] in list:
            list.remove(s[l])
            l+=1
        list.append(s[r])
        max_len = max(max_len, r-l+1)
    return max_len



s = "bbbbb"
print(longest_substring(s))