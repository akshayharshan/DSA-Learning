# Heap pop
# Heap push
# Heap peak

# Time complexity of heap push and pop are O(log(n))
# Heap sort is O(nlog(n))


# Min heap
import heapq

heap = []

heapq.heappush(heap,3)
heapq.heappush(heap,4)
heapq.heappush(heap,5)

print(heapq.heappop(heap))

# Max heap
maxheap = []


heapq.heappush(maxheap,-5)
heapq.heappush(maxheap,4)
heapq.heappush(maxheap,-3)
heapq.heappush(maxheap,-11)

print(heapq.heappop(maxheap))