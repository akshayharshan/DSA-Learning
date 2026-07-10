
def longest_substring(s):

    hashmap = []
    l = 0
    max_len = 0
    for r in range(len(s)):
        while s[r] in hashmap:
            hashmap.remove(s[l])
            l += 1
        hashmap.append(s[r])
        max_len = max(r - l +1,max_len)
    return max_len





s = "abcabcbb"

print(longest_substring(s))