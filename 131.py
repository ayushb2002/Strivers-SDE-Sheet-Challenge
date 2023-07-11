class   TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None


def construct(start, end, postorder, pIndex, d):
 
    if start > end:
        return None, pIndex
    root = TreeNode(postorder[pIndex])
    pIndex = pIndex - 1
    index = d[root.data]
 
    root.right, pIndex = construct(index + 1, end, postorder, pIndex, d)
    root.left, pIndex = construct(start, index - 1, postorder, pIndex, d)
    return root, pIndex
def getTreeFromPostorderAndInorder(postorder, inorder):
    n = len(inorder)
    d = {}
    for i, e in enumerate(inorder):
        d[e] = i
    pIndex = n - 1
    return construct(0, n - 1, postorder, pIndex, d)[0]