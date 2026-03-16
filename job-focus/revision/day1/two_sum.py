def two_sum(nums, target):

    hashmap = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in hashmap:
            return [hashmap[compliment],i]
            
        hashmap[nums[i]] = i






nums = [3,2,4]
target = 6

print(two_sum(nums,target))