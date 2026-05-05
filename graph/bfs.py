from collections import deque


A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

from collections import defaultdict

D = defaultdict(list)

for u, v in A:
  D[u].append(v)



print(D)

source = 0
seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
   node =  q.popleft()
   print(node)

   for neib_node in D[node]:
      if neib_node not in seen:
         seen.add(neib_node)
         q.append(neib_node)
   