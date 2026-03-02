def two_sum(nums,target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return hashmap[complement], i
        hashmap[nums[i]] = i



nums = [3,2,4]
target = 6
print(two_sum(nums,target))