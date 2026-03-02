def longest_substring(string):

    l = 0
    max_len = 0
    hashmap = set()

    for r in range(len(string)):
        while hashmap and string[r] in hashmap:
            hashmap.remove(string[l])
            l+=1
        hashmap.add(string[r])
        max_len = max(max_len, r-l+1)
    return max_len




print(longest_substring('abcabcbb'))