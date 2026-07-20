def valid_anagram(s,t):
    hashmap = {}
    s = list(s)
    t = list(t)
    for char in s:
        hashmap[char] = hashmap.get(char,0) + 1
    for char in t:
        if not hashmap.get(char):
            return False
        if hashmap[char] != 0:
            hashmap[char] -= 1
            if hashmap[char] == 0:
                hashmap.pop(char)
            
    return False if hashmap else True

    


s = "anagram"
t = "nagaram"

print(valid_anagram(s,t))

