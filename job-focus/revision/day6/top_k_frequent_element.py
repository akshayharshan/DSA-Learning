import heapq
def top_k_frequent_element(nums,k):
    hashmap = {}
    heap = []
    res = []
    for num in nums:
        hashmap[num] = hashmap.get(num,0) + 1
    for key,value in hashmap.items():
        heapq.heappush(heap,(value,key))

        if len(heap) > k:
            heapq.heappop(heap)

    for _ in heap:
        key,value = heapq.heappop(heap)
        print(heap)
        res.append(value)
    return res

nums = [1,1,1,2,2,3]
k = 2
top_k_frequent_element(nums,k)