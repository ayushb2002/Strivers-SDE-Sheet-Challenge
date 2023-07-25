def isGraphBirpartite(edges):
    n = len(edges)
    queue = [0]
    color = [-1]*n
    for i in range(n):
        for j in range(len(edges[i])):
            if edges[i][j] == 1:
                edges[i][j] = j
    
    color[0] = 0
    while queue:
        node = queue.pop(0)
        
        for n in edges[node]:
            if color[n] == -1:
                color[n] = not color[node]
                queue.append(n)
            else:
                if color[n] == color[node]:
                    return False
                
    return True
