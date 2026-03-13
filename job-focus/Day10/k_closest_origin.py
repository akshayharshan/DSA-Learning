import heapq
def k_closest_origin(points,k):
    heap =[]
    res = []
    for i in range(len(points)):
        result = points[i][0] * points[i][0] + points[i][1] * points[i][1]
        heapq.heappush(heap,(result,points[i]))
    

    for _ in range(k):
        value = heap.pop()
        res.append(value[1])
    return res


        

points = [[1,3],[-2,2],[3,4]]
k = 2

print(k_closest_origin(points,k))

#k_closest_origin(points,k)