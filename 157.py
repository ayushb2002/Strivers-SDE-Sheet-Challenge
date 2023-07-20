class graphNode:
    def __init__(self, *args):
        if(len(args) == 0):
            self.data = 0
            self.neighbours = []

        elif(len(args) == 1):
            self.data = args[0]
            self.neighbours = []

        elif(len(args) == 2):
            self.data = args[0]
            self.neighbours = args[1]

    def __del__(self):
        self.neighbours.clear()


def cloneGraph(node):
    hm = {}

    def dfs(node):
        if node in hm:
            return hm.get(node)
        
        clone = graphNode(node.data)
        hm[node] = clone
        
        for n in node.neighbours:
            clone.neighbours.append(dfs(n))

        return clone
    
    clone = dfs(node)
    return clone