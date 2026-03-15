def first_unique_char(string):
    hashmap = {}
    for char in string:
        hashmap[char] = hashmap.get(char,0)+1
    for i in range(len(string)):
        if hashmap[string[i]] == 1:
            return i



print(first_unique_char("loveleetcode"))