def prefix_sum(nums,k):

    count=0
    hashmap = {0:1}
    prefix_sum = 0

    for num in nums:
        prefix_sum += num
        prev_sum = prefix_sum - k

        if prev_sum in hashmap:
            count += hashmap[prev_sum]
        hashmap[prefix_sum] = hashmap.get(prefix_sum,0) + 1
    return count








nums = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7

print(prefix_sum(nums,k))