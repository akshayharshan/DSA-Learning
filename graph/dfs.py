A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

from collections import defaultdict

D = defaultdict(list)

for u, v in A:
  D[u].append(v)



print(D)

# Recursive method
def dfs(node,visited):
  print(node)
  for nei_node in D[node]:
    if nei_node not in visited:
       dfs(nei_node,visited)
  
source = 0
visited = set()
dfs(source,visited)


# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A', 'D'],
#     'D': ['B', 'C']
# }

# def dfs(node, visited):
#     visited.add(node)
#     print(node)

#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             dfs(neighbor, visited)

# visited = set()
# dfs('A', visited)


# Iterative method

source = 0
seen = set()
seen.add(source)
stack = [source]

while stack:
    node = stack.pop()
    print(node)
    for neib_node in stack[node]:
        if neib_node not in seen:
            stack.add(neib_node)
            stack.append(neib_node)