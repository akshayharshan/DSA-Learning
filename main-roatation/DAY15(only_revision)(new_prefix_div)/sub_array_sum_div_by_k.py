def subarray_div_by_k(nums,k):

    prefix_sum = 0
    hashmap = {0:-1}

    for i in range(len(nums)):

        prefix_sum +=nums[i]
        prev_div = prefix_sum % k

        if prev_div in hashmap:
            if i - hashmap[prev_div] >= 2:
                return True
        else:
            hashmap[prefix_sum % k] = i
    return hashmap





nums = [23, 2, 4, 6, 7]
k = 6
print(subarray_div_by_k(nums,k))



