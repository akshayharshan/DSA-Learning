A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]
from collections import defaultdict

D = defaultdict(list)

for u,v in A:
    D[u].append(v)

def dfs(node,visited):
    print(node)
    for neib_node in D[node]:
        if neib_node not in visited:
            visited.add(neib_node)
            dfs(neib_node,visited)




visited = set()
dfs(0,visited)