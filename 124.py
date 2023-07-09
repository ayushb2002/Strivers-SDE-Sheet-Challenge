class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

def isBalancedBT(root):
    flag = True
    def trav(root):
        if not root:
            return 0
        l = trav(root.left)
        r = trav(root.right)
        nonlocal flag
        if abs(l-r) > 1:
            flag = False

        return 1+max(l, r)
    
    trav(root)
    return flag