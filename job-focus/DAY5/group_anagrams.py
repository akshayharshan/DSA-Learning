def group_anangram(strings):
    hashmap = {}
    for string in strings:
        sorted_text = "".join(sorted(string))
        if sorted_text not in hashmap:
            hashmap[sorted_text] = []
        hashmap[sorted_text].append(string)
    return list(hashmap.values())






print(group_anangram(["eat","tea","tan","ate","nat","bat"]))