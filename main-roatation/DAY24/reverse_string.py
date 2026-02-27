def reverse_string(string):

    l=0
    r =len(string)-1
    array = list(string)
    new_str = ''

    while l < r:
        array[l],array[r] = array[r],array[l]
        l+=1
        r-=1
    for char in array:
        new_str += char
    return new_str

string = "hello"
print(reverse_string(string))