def detectCycleInDirectedGraph(n, edges):
    graph = [[] for _ in range(n)]
    for i in range(len(edges)):
        graph[edges[i][0]-1].append(edges[i][1]-1)
    
    visited = [0]*n

    def dfs(node):

        visited[node] = 1

        for n in graph[node]:
            if not visited[n]:
                flag = dfs(n)
                if flag:
                    return True
            else:
                return True
        
        visited[node] = 0
        return False

    for i in range(n):
        if not visited[i]:
            res = dfs(i)
            if res:
                return True
    
    return False