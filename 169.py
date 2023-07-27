import heapq as hq

def calculatePrimsMST(n, m, g):
    pq = [(0, 0, -1)]
    visited = [0]*n
    res = []
    graph = [[] for _ in range(n)]
    for u, v, w in g:
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))

    while pq:
        w, node, par = hq.heappop(pq)

        if visited[node]:
            continue
        else:
            visited[node] = 1

        if par != -1:
            res.append([par+1, node+1, w])

        for ne, we in graph[node]:
            hq.heappush(pq, (we, ne, node))

    return res