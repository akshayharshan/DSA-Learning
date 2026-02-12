def prefixsum(nums,k):

    prefixsum=0
    hashmap = {0:1}
    count=0

    for r in range(len(nums)):
        prefixsum+= nums[r]
        prevsum = prefixsum - k
        if prevsum in hashmap:
            count+=hashmap[prevsum]
        hashmap[prefixsum] = hashmap.get(prefixsum,0)+1

    return count

arr = [1, 1, 1]
k = 2

print(prefixsum(arr,k))