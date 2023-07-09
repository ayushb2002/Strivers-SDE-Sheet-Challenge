class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lowestCommonAncestor(root, x, y):
	
    def trav(root):
        if root is None or root.data == x or root.data == y:
            return root

        left = trav(root.left)
        right = trav(root.right)

        if not left:
            return right
        elif not right:
            return left
        else:
            return root

    x = trav(root)
    return x.data