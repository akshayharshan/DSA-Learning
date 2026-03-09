def first_unique_char(s):

    hashmap = {}

    for char in s:
        hashmap[char] = hashmap.get(char,0) + 1
    for i,char in enumerate(s):
        if hashmap[char] == 1:
            return i
    return -1





print(first_unique_char("aabb"))
