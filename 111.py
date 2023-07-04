def getInOrderTraversal(root):
    res = []

    def inorder(root):
        if not root:
            return
        
        inorder(root.left)
        res.append(root.data)
        inorder(root.right)
    
    inorder(root)
    return res