class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def isLeaf(root):
    if not root.left and not root.right:
        return True
    
    return False

def findMaxSumPath(root):
    if not root:
        return -1
    res, leaf = 0, 0
    def trav(root):
        if not root:
            return 0
        
        nonlocal leaf
        if isLeaf(root):
            leaf += 1
        
        l = trav(root.left)
        r = trav(root.right)
        nonlocal res
        res = max(res, root.val+l+r)
        return (root.val + max(l, r))

    trav(root)

    return res if leaf > 1 else -1