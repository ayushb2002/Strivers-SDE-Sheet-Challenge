class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diameterOfBinaryTree(root):
    diameter=0
    def f(root):
        if root==None:return 0

        Left=f(root.left)
        Right=f(root.right)
        nonlocal diameter
        diameter=max(diameter,Left+Right)
        return 1+max(Left,Right)
    
    f(root)
    return diameter