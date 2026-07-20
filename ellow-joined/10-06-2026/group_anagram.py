def group_anangram(strs):
    hashmap = {}
    result = []
    for word in strs:
        sorted_list = sorted(word)
        sorted_word = ''.join(sorted_list)
        if hashmap.get(sorted_word):
            hashmap[sorted_word].append(word)
        else:
            hashmap[sorted_word] = [word]
    return list(hashmap.values())
        


strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anangram(strs))
