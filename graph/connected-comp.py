def countComponents(n, edges):
    graph = {i: [] for i in range(n)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0

    def dfs(node):
        for nei_node in graph[node]:
            if nei_node not in visited:
                dfs(nei_node,visited)


    for i in range(n):
        if i not in visited:
            count += 1
            dfs(i)

    return count