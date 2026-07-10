def valid_anagram(s,t):
    s_hash_map = {}

    for i in range(len(s)):
        s_hash_map[s[i]] = s_hash_map.get(s[i],0) + 1
    
    for j in range(len(t)):
        if not s_hash_map.get(t[j],False):
            return False
        else:
            s_hash_map[s[j]] -= 1
            if s_hash_map[s[j]] == 0:
                s_hash_map.pop(s[j])
    return not s_hash_map




s = "anagram"
t = "nagaram"
print(valid_anagram(s,t))