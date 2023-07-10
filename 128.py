class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isLeaf(root):
    if not root.left and not root.right:
        return True

    return False

def leftTraversal(root, res):
    node = root.left
    while node:
        if not isLeaf(node):
            res.append(node.data)
        if node.left:
            node = node.left
        else:
            node = node.right

    return

def rightTraversal(root, store):
    node = root.right
    res = []
    while node:
        if not isLeaf(node):
            res.append(node.data)
        if node.right:
            node = node.right
        else:
            node = node.left
    
    res.reverse()
    for i in res:
        store.append(i)

    return

def leafTraversal(root, store):
    if isLeaf(root):
        store.append(root.data)
        return

    if root.left:
        leafTraversal(root.left, store)
    if root.right:
        leafTraversal(root.right, store)

def traverseBoundary(root):
    if not root:
        return []
    res = []

    if not isLeaf(root):
        res.append(root.data)
    
    leftTraversal(root, res)
    leafTraversal(root, res)
    rightTraversal(root, res)

    return res
    