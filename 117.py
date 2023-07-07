class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    inord = []
    preord = []
    postord = []
    def inorder(root):
        if not root:
            return 

        inorder(root.left)
        inord.append(root.data)
        inorder(root.right)
    
    def preorder(root):
        if not root:
            return 

        preord.append(root.data)
        preorder(root.left)
        preorder(root.right)

    def postorder(root):
        if not root:
            return 

        postorder(root.left)
        postorder(root.right)
        postord.append(root.data)    

    inorder(root)
    preorder(root)
    postorder(root)

    return [inord, preord, postord]