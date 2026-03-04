def valid_anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    hashmap = {}

    for char in str1:
        hashmap[char] = hashmap.get(char,0)+1

    for char in str2:
        if char in hashmap:
            hashmap[char] -= 1
            if hashmap[char] == 0:
                del hashmap[char]
        else:
            return False
    return True if not hashmap else False




print(valid_anagram("listen","silent"))