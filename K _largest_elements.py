import heapq

class Solution:
    def kLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap


    
nums = [3, 2, 1, 5, 6, 4]
k = 3

result = Solution()
print(result.kLargest(nums,k))