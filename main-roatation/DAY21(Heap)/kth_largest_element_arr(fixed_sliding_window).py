import heapq
def kth_largest_element(arr,k):

    heap = []
    for num in arr:
        heapq.heappush(heap,num)
        if(len(heap) > k):
            heapq.heappop(heap)
    return heap[0] if heap else  None




arr = [3,2,1,5,6,4]
k= 2
print(kth_largest_element(arr,k))


# complexity is O(nlogk)
