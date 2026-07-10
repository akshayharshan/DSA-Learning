def two_sum(nums,target):
    hashmap = {}

    for i in range(len(nums)):
        negate = target - nums[i]

        if negate in hashmap:
            return hashmap[negate],i
        hashmap[nums[i]] = i


nums = [2,7,11,15]
target = 9

print(two_sum(nums,target))