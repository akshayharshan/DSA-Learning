import heapq


def top_k_element(nums,k):

    heap = []
    hashmap = {}
    result = []

    for num in nums:  # O(n)
        hashmap[num] = hashmap.get(num,0)+1
    for num,freq in hashmap.items(): # o(nlogk)
        heapq.heappush(heap,(freq,num))
        if len(heap) > k:
            heapq.heappop(heap)
    while heap: # while loop is o(n) but the heap have O(logk) so it will become klog(k)
        freq,num = heapq.heappop(heap)
        result.append(num)
    return result
        
# so final it will be nlog(k)

nums = [1,1,1,2,2,3]
k = 2
print(top_k_element(nums,k))