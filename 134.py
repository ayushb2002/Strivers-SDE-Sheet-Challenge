def invertBinaryTree(r, l):
    q = False
    ans = None

    def s(r, p, l):
        nonlocal q, ans
        if not r:
            return

        if r.data == l:
            r.left = p
            q = True
            ans = r
            return

        s(r.left, r, l)

        if q:
            r.left = p
            return

        s(r.right, r, l)

        if q:
            if r.left:
                r.right = r.left
            else:
                r.right = None
            r.left = p
            return

    s(r, None, l)
    return ans