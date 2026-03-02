def reverse_string(string):
    new_str = list(string)
    l,r = 0,len(new_str) - 1
    while l < r:
        new_str[l],new_str[r] = new_str[r],new_str[l]
        l+=1
        r-= 1
    return "".join(new_str)



string = "hello"
print(reverse_string(string))