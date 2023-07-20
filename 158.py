from typing import *

def depthFirstSearch(V, E, edges):
    graph = [ [] for _ in range(V) ]
    for e1, e2 in edges:
        graph[e1].append(e2)
        graph[e2].append(e1)
    
    visited = [0]*V
    res = []

    def dfs(node):
        if visited[node]:
            return
        
        visited[node] = 1
        res.append(node)

        for n in graph[node]:
            dfs(n)
    
    ans = []
    for i in range(V):
        if not visited[i]:
            dfs(i)
            ans.append(sorted(res))
            res = []

    return ans

V, E = 5, 4
edges = [[0, 2],
        [0, 1],
        [1, 2],
        [3, 4]]

print(depthFirstSearch(V, E, edges))