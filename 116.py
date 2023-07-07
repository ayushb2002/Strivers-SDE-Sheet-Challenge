class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def getTopView(root):
    if not root:
        return []
    queue = [(root, 0)]
    hm = {}
    minLev, maxLev = float('inf'), float('-inf')
    while queue:
        node, lev = queue.pop(0)
        if not hm.get(lev):
            hm[lev] = node.val
        
        minLev = min(minLev, lev)
        maxLev = max(maxLev, lev)

        if node.left:
            queue.append((node.left, lev-1))

        if node.right:
            queue.append((node.right, lev+1))

    res = []
    for lev in range(minLev, maxLev+1):
        res.append(hm.get(lev))

    return res