def prefix_sum(nums,k):
    hashmap = {0:1}
    prefix_sum = 0
    count = 0

    for r in range(len(nums)):
        prefix_sum += nums[r]

        prev_sum = prefix_sum - k

        if prev_sum in hashmap:
            count += hashmap[prev_sum]
        hashmap[prefix_sum] = hashmap.get(prefix_sum,0) + 1

    return count










nums = [1,1,1]
k = 2
print(prefix_sum(nums,k))