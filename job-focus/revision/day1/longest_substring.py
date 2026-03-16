def longest_substring(string):
    hashmap = set()
    l = 0
    max_len = 0
    for r in range(len(string)):
        while string[r] in hashmap:
            hashmap.remove(string[l])
            l+=1
        hashmap.add(string[r])
        max_len = max(max_len,r-l+1)
    
    return max_len
    
    
    
s = "abcabcbb"   
print(longest_substring(s))