def two_sum(numbers,target):
    hashmap={}
    for i in range(len(numbers)):
        negate = target - numbers[i]
        for negate  in hashmap:
            return [hashmap[negate] + 1 , i +1]
        hashmap[numbers[i]] = i   


print(two_sum([[2,3,4]],6))