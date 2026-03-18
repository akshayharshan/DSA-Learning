def sub_arr_equals_k(nums,k):
    hashmap = {0:1}
    prefix_sum = 0
    counter= 0
    for r in range(len(nums)):
        prefix_sum += nums[r]
        prev_sum = prefix_sum - k
        if prev_sum in hashmap:
            counter += hashmap[prev_sum]
        hashmap[prefix_sum] = hashmap.get(prefix_sum,0)+1
    return counter


nums = [1,1,1]
k = 2
print(sub_arr_equals_k(nums,k))