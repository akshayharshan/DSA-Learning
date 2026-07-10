
def groupAnagram(strs):

    hashmap = {}

    for str in strs:
        new_list = list(str)
        new_list.sort()
        new_str = ''.join(new_list)

        if not hashmap.get(new_str):
            hashmap[new_str] = []
        
        hashmap[new_str].append(str)
    return hashmap.values()







strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagram(strs))