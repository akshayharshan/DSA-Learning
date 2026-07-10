
def group_anagram(strs):
    hashmap = {}
    result = []
    for word in strs:
        new_list = list(word)
        new_list.sort()
        new_str = ''.join(new_list)
        if not hashmap.get(new_str):
            hashmap[new_str] = []
        hashmap[new_str].append(word)
        
    for value in hashmap.values():
        result.append(value)

    return result







strs = ["eat","tea","tan","ate","nat","bat"]

print(group_anagram(strs))