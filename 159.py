def BFS(vertex, edges):
    graph = [[] for _ in range(vertex)]
    for i in range(len(edges[0])):
        v = edges[0][i]
        e = edges[1][i]
        graph[v].append(e)
        graph[e].append(v)
    
    for i in range(vertex):
        graph[i].sort()
        
    queue = [0]
    visited = [0]*vertex
    res = []

    while queue:
        node = queue.pop(0)
        if not visited[node]:
            res.append(node)
            visited[node] = 1
            for n in graph[node]:
                if not visited[n]:
                    queue.append(n)
    
    for i in range(vertex):
        if not visited[i]:
            res.append(i)
    
    return res