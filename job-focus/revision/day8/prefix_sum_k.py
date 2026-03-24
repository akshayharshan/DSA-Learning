def prefix_sum_k(nums,k):
    count = 0
    hashmap = {0:1}
    prefix_sum  = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]

        prev_sum = prefix_sum - k

        if prev_sum in hashmap:
            count += hashmap[prev_sum]
        hashmap[prefix_sum] = hashmap.get(prefix_sum,0)+1
    return count