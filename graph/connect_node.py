graph = { i : [] for i in range(5)}

print(graph)

for u,v in [(0,1),(1,2),(2,3),(3,4)]:
    graph[u].append(v)
    graph[v].append(u)

print(graph)

count = 0
def dfs(node):
    for nei_mode in graph[node]:
        visited.add(node)
        if nei_mode not in visited:
            visited.add(nei_mode)
            dfs(nei_mode)


visited = set()
for i in graph:
    if i not in visited:
        count +=1
        dfs(i)

print(count)