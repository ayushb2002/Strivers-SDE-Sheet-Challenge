def kthSmallest(root, k):
    count = 0
    res = -1
    def inord(root):
        nonlocal count, res
        if not root:
            return
        
        inord(root.left)
        count += 1
        if count == k:
            res = root.data
        inord(root.right)

    inord(root)
    return res