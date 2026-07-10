def valid_anagram(s,t):
    first_hashmap = {}
    second_hashmap = {}

    if len(s) != len(t):
        return False
    

    for char in s:
        first_hashmap[char] = first_hashmap.get(char,0) + 1
    for char in t:
        second_hashmap[char] = second_hashmap.get(char,0) + 1

    return first_hashmap == second_hashmap
    


    





s = "anagram"
t = "nagaram"

print(valid_anagram(s,t))