def bellmonFord(n, m, src, dest, edges):
    
    dist = [float('inf')]*n
    dist[src-1] = 0

    for _ in range(n-1):
        for i in range(m):
            u, v, w = edges[i]
            if dist[u-1] + w < dist[v-1]:
                dist[v-1] = dist[u-1] + w
            
    return 10**9 if dist[dest-1] == float('inf') else dist[dest-1]