def topk_freq_element(nums,k):
    hashmap = {}
    result = []
    for i in range(len(nums)):
        hashmap[nums[i]] = hashmap.get(nums[i],0)+1
    
    arr = sorted(hashmap.items(),key=lambda x : x[1], reverse=True)

    for i in range(k):
        result.append(arr[i][0])
    return result









nums = [1,1,1,2,2,3]
k = 2
print(topk_freq_element(nums,k))
