def getPostOrderTraversal(root):
    res = []

    def trav(root):
        if not root:
            return
        
        trav(root.left)
        trav(root.right)
        res.append(root.data)

    trav(root)
    return res