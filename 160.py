def cycleDetection(edges, n, m):
    graph = [[] for _ in range(n)]
    for v, e in edges:
        graph[v-1].append(e-1)
        graph[e-1].append(v-1)
    
    visited = [0]*n

    def dfs(node, prev):
        
        visited[node] = 1

        for n in graph[node]:
            if not visited[n]:
                flag = dfs(n, node)
                if flag:
                    return True
            elif prev != n:
                return True

        return False

    for i in range(n):
        if not visited[i]:
            flag = dfs(i, -1)
            if flag:
                return "Yes"
    
    return "No"