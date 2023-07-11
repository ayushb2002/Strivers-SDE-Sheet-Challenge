class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def buildBinaryTree(preorder:list, inorder:list):
    VAL_TO_INORDER_IDX = {inorder[i]: i for i in range(len(inorder))}
    def buildTreePartition(preorder, inorder_start, inorder_end):
        if not preorder or inorder_start < 0 or inorder_end > len(inorder):
            return None

        root_val = preorder[0]
        root_inorder_idx = VAL_TO_INORDER_IDX[root_val]
        if root_inorder_idx > inorder_end or root_inorder_idx < inorder_start:
            return None

        root = BinaryTreeNode(preorder.pop(0))
        root.left = buildTreePartition(preorder, inorder_start, root_inorder_idx - 1)
        root.right = buildTreePartition(preorder, root_inorder_idx + 1, inorder_end)

        return root

    return buildTreePartition(preorder, 0, len(inorder) - 1)