import heapq
def findKthLargest(nums ,k):
        heap = []
        hashmap = set()
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap,num)
            else:
                val = heapq.heappushpop(heap,num)
                hashmap.add(val)
        return heap[0]


nums = [3,2,1,5,6,4]
k = 2

print(findKthLargest(nums,k))