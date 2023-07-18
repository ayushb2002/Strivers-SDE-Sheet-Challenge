
def BTtoDLL(root):
    prev, head = None, None

    def inorder(root):
        nonlocal prev, head
        if not root:
            return

        inorder(root.left)
        if not prev:
            head = root
        else:
            root.left = prev
            prev.right = root
        prev = root
        inorder(root.right)

    inorder(root)
    return head