def prefix_sum(nums,k):
    count = 0
    map = {0:1}
    prefix_sum = 0
    for i in range(len(nums)):
        prefix_sum +=nums[i]

        prev_sum = prefix_sum - k
        if prev_sum in map:
            count += map[prev_sum]
            map[prev_sum]=map.get(prev_sum,0) +1
        map[prefix_sum] = map.get(prefix_sum, 0) + 1

    return count

        






nums = [1, 2, 3]
k = 3
print(prefix_sum(nums,k))