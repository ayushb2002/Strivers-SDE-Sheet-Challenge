def topologicalSort(adj, v, e):
    stack = []
    visited = [0] * v
    graph = [[] for _ in range(v)]
    for i in range(e):
        graph[adj[i][0]].append(adj[i][1])

    def dfs(node):
        
        visited[node] = 1

        for n in graph[node]:
            if not visited[n]:
                dfs(n)
        
        stack.insert(0, node)
    
    for i in range(v):
        if not visited[i]:
            dfs(i)

    return stack