# BinaryTreeNode class definition
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def zigZagTraversal(root):
    if not root:
        return []
    queue = [(root, 1)]
    trav = {}
    last = float('-inf')
    while queue:
        node, lev = queue.pop(0)
        if trav.get(lev):
            trav[lev].append(node.data)
        else:
            trav[lev] = [node.data]
        last = max(last, lev)
        if node.left:
            queue.append((node.left, lev+1))
        if node.right:
            queue.append((node.right, lev+1))
    
    res = []
    for i in range(1, last+1):
        if i%2 == 0:
            res += trav[i][::-1]
        else:
            res += trav[i]
    
    return res