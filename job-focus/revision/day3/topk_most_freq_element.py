import heapq
def topk_most_freq_element(nums,k):
    hashmap = {}
    heap = []
    for i in nums:
        hashmap[i] = hashmap.get(i,0) + 1

    for key,value in hashmap.items():
        heapq.heappush(heap,(value,key))
        if len(heap) > k:
            heapq.heappop(heap) 
    res=[]   
    for _ in range(len(heap)):
        frq,val = heapq.heappop(heap)
        res.append(val)
    return res




nums = [1,1,1,1,2,3,4,5]
k = 1
print(topk_most_freq_element(nums,k))