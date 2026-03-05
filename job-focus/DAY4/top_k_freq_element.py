import heapq
def top_k_freq_element(nums,k):
    heap = []
    hashmap = {}

    for num in nums:
        hashmap[num] = hashmap.get(num,0)+1

    for num,freq in hashmap.items():
        heapq.heappush(heap,(freq,num))
        if len(heap) > k:
            heapq.heappop(heap)
    result =[]
    while heap:
        freq,num = heapq.heappop(heap)
        result.append(num)
    return result

# push and pop of the element is o(logk)

# frequnecy opeartion O(n)

# Heap opeartion O(nlogk)

# total o(nlogk)

#space o(n)

nums = [1,1,1,2,2,3]
k = 2
print(top_k_freq_element(nums,k))