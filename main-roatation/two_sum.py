def two_sum(nums,target):
    l,r=0,len(nums)-1
    hashmap = {}
    for i,num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [i,hashmap[diff]]
        hashmap[num] = i 




nums = [-3, -1, 0, 2, 4, 5]
target = 1
print(two_sum(nums,target))