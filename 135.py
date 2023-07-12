def changeTree(root): 
    
    def dfs(node):
        if not node: 
            return 0
        if not node.left and not node.right: 
            node.data = 10**6
        else: 
            node.data = dfs(node.left) + dfs(node.right)
        
        return node.data
    
    dfs(root)
    return root