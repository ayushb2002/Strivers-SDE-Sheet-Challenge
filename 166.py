import heapq

def dijkstra(vec, vertices, edges, source):
    graph = [[] for _ in range(vertices)]
    for u, v, w in vec:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    dist = [2147483647]*vertices
    dist[source] = 0

    pq = [(0, source)]

    while pq:
        w, node = heapq.heappop(pq)
        for n, wei in graph[node]:
            if dist[n] > w+wei:
                dist[n] = w+wei
                heapq.heappush(pq, (w+wei, n))
    
    return dist