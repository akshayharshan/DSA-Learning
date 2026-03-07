def longest_substring_without_char(string):

    map = set()
    l= 0
    str_len = 0
    for r in range(0,len(string)):
       
        while string[r] in map:
            map.remove(string[l])
            l+=1
        else:
            map.add(string[r])
            str_len = max(str_len,r-l+1)          

        
    return str_len
        








print(longest_substring_without_char("abcabcbb"))


