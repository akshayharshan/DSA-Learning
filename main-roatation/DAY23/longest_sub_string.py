def longest_sub_string(string):
    seen = set()
    l =0
    max_len = 0
    for r in range(len(string)):
        
        while string[r] in seen:
            seen.remove(string[l])
            l+=1
        seen.add(string[r])
        max_len = max(max_len,r-l+1)
    return max_len




string = "abcabcbb"
print(longest_sub_string(string))