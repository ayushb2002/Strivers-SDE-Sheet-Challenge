def findCeil(root, X):
    ans = -1
    while root:
        if root.data == X:
            ans = X
            break
        if root.data > X:
            ans = root.data
            root = root.left if root.left else None
        elif root.data < X:
            root = root.right if root.right else None
        
    return ans