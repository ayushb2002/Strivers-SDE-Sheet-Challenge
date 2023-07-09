class BinaryTreeNode:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
        
def identicalTrees(root1, root2):
    
    if root1==None and root2==None:
        return True
    if (root1!=None and root2==None) or (root1==None and root2!=None):
        return False
    
    left=identicalTrees(root1.left,root2.left)
    right=identicalTrees(root1.right,root2.right)
    val=root1.data==root2.data

    if left and right and val:
        return True
    else:
        return False