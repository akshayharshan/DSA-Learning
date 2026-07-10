def topkfreq(nums,k):
    hashmap = {}
    result = []
    for num in nums:
        hashmap[num] = hashmap.get(num,0)+1
    arr = sorted(hashmap.items(),key = lambda x : x[1],reverse=True)

    for i in range(k):
        result.append(arr[i][0])

    return result




nums = [1,2,1,2,1,2,3,1,3,2]
k = 2

print(topkfreq(nums,k))