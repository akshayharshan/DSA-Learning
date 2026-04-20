# Let 'S'= “abAb”. 

# Here the characters ‘a’ and ‘A’ have frequency 1 and character ‘b’ has frequency ‘2’.  

# Therefore the sorted string is “bbAa”. 


def sort_string(s):
    hashmap = {}
    s = sorted(s)
    for j in range(len(s)):
        i = -j-1
        hashmap[s[i]] = hashmap.get(s[i],0) + 1
    newstr = ''
    for key,value in hashmap.items():
        for s in range(value):
            newstr +=key
    return newstr



s = "abAb"
print(sort_string(s))