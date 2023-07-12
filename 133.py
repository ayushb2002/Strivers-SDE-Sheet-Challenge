class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def flattenBinaryTree(root):
    prev = None

    def flatten(node):
        nonlocal prev
        if not node:
            return
        
        flatten(node.right)
        flatten(node.left)

        node.right = prev
        node.left = None
        prev = node
    
    flatten(root)
    
    return root