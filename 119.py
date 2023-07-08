from typing import List

class TreeNode:   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pathInATree(root: TreeNode, x: int) -> List[int]:
    path = []

    def trav(root):
        if not root:
            return False
        
        path.append(root.data)
        if root.data == x:
            return True

        if trav(root.left) or trav(root.right):
            return True
        
        path.pop()
        return False

    trav(root)
    return path