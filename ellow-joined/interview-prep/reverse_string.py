def reverse_string(s):
    l = 0 
    r = len(s) - 1
    str_array = list(s)
    while l < r:
        str_array[l],str_array[r] = str_array[r],str_array[l]
        l+=1
        r-=1
    return ''.join(str_array)


print(reverse_string("hello"))