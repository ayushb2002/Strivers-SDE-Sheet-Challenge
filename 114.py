class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getLeftView(root)->list:
    res = []
    trav = []
    def inord(root, i):
        if not root:
            return
        
        if i not in trav:
            res.append(root.data)
            trav.append(i)

        inord(root.left, i+1)
        inord(root.right, i+1)

    inord(root, 0)
    return res