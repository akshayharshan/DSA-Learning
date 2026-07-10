def top_k_element(nums,k):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = hashmap.get(nums[i],0)+1

    result = []

    arr = sorted(hashmap.items(),key=lambda x : x[1] , reverse=True)
    
    for i in range(k):
        result.append(arr[i][0])
    return result


nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
print(top_k_element(nums,k))