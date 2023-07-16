def KthLargestNumber(root, k):
    res = []
    def inord(root):
        if not root:
            return

        inord(root.left)
        res.append(root.data)
        inord(root.right)

    inord(root)

    res.reverse()

    if len(res) < k:
        return -1
    
    return res[k-1]