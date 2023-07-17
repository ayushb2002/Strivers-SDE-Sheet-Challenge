def largestBST(root):
    
    def preorder(root):
        if not root:
            return (float('inf'), float('-inf'), 0)
        
        lMin, lMax, lCount = preorder(root.left)
        rMin, rMax, rCount = preorder(root.right)

        if lMax < root.data and root.data < rMin:
            return (min(root.data, lMin), max(root.data, rMax), 1+lCount+rCount)
        
        return (float('-inf'), float('inf'), max(lCount, rCount))

    mx, mn, c = preorder(root)

    return c