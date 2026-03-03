import heapq
def kth_largest_element(nums,k):

    heap = []

    for num in nums:
        heapq.heappush(heap,num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]






# print(kth_largest_element([3,2,1,5,6,4],2))


# def kth_largest_element(nums,k):
#     max_heap = [-num for num in nums]



# print(kth_largest_element([3,2,1,5,6,4],2))