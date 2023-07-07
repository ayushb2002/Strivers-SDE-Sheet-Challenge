class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

	
def bottomView(root):
    queue = [(root, 0)]
    hm = {}
    minLev, maxLev = float('inf'), float('-inf')
    while len(queue) > 0:
        node, lev = queue.pop(0)
        if node.left:
            queue.append((node.left, lev-1))
        
        if node.right:
            queue.append((node.right, lev+1))
        
        hm[lev] = node.data
        minLev = min(lev, minLev)
        maxLev = max(lev, maxLev)
    
    res = []
    for lev in range(minLev, maxLev+1):
        res.append(hm[lev])
        
    return res

