class DisjointSet:
    def __init__(self, n):
        self.rank = [0]*(n+1)
        self.size = [1]*(n+1)
        self.parent = []
        for i in range(n+1):
            self.parent.append(i)
        
    def findUPar(self, node):
        """Finding the ultimate parent of a node"""
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    def unionByRank(self, u, v):
        ult_u = self.findUPar(u)
        ult_v = self.findUPar(v)
        if ult_u == ult_v:
            return
        
        if self.rank[ult_u] < self.rank[ult_v]:
            self.parent[ult_u] = ult_v
        elif self.rank[ult_v] < self.rank[ult_u]:
            self.parent[ult_v] = ult_u
        else:
            self.parent[ult_v] = ult_u
            self.rank[ult_u] += 1

    def unionBySize(self, u, v):
        ult_u = self.findUPar(u)
        ult_v = self.findUPar(v)
        if ult_u == ult_v:
            return
        if self.size[ult_u] < self.size[ult_v]:
            self.parent[ult_u] = ult_v
            self.size[ult_v] += self.size[ult_u]
        else:
            self.parent[ult_v] = ult_u
            self.size[ult_u] += self.size[ult_v]
        

def kruskalMST(n, m, graph):
    ds = DisjointSet(n)
    res = 0
    graph.sort(key=lambda x:x[2])
    for u, v, w in graph:
        if ds.findUPar(u) != ds.findUPar(v):
            res += w
            ds.unionBySize(u, v)

    return res