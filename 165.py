def storeByFinishingTime(n, graph):
    stack = []
    visited = [0]*n
    def dfs(node):
        visited[node] = 1
        for n in graph[node]:
            if not visited[n]:
                dfs(n)

        stack.insert(0, node)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return stack

def reverseGraph(n, graph):
    revG = [[] for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            revG[j].append(i)

    return revG

def stronglyConnectedComponents(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
    time = storeByFinishingTime(n, graph)
    graph = reverseGraph(n, graph)
    visited = [0]*n
    res = []
    temp = []
    def dfs(node):
        visited[node] = 1
        temp.append(node)
        for n in graph[node]:
            if not visited[n]:
                dfs(n)
    
    for i in time:
        if not visited[i]:
            dfs(i)
            res.append(temp)
            temp = []

    return res