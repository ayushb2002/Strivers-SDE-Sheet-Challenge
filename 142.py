def predecessorSuccessor(root, key):
    res = []
    def inorder(root):
        if not root:
            return
        
        inorder(root.left)
        res.append(root.data)
        inorder(root.right)

    inorder(root)
    curr = res.index(key)
    return [res[curr-1] if curr-1 >= 0 else -1, res[curr+1] if curr+1 < len(res) else -1]