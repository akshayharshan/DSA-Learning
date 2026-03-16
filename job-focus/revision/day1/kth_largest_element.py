import heapq
def kth_largest_element(nums,k):
    heap=[]
    for num in nums:
        heapq.heappush(heap,num)
        
        if len(heap) > k:
            heapq.heappop(heap)
       
    return heap[0]


# here the time complexity is nlogk



nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(kth_largest_element(nums,k))