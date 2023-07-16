class   TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right


def LCAinaBST(root, P, Q):

    def trav(root):
        if not root or root == P or root == Q:
            return root

        l = trav(root.left)
        r = trav(root.right)

        if not l:
            return r
        elif not r:
            return l
        else:
            return root
        
    x = trav(root)

    return x