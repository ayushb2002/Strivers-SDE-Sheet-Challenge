def connectNodes(root):
    queue = [(root, 0)]
    hm = {}
    maxLev = 0
    while queue:
        node, lev = queue.pop(0)
        maxLev = max(maxLev, lev)
        if hm.get(lev):
            hm[lev].append(node)
        else:
            hm[lev] = [node]

        if node.left:
            queue.append((node.left, lev+1))
        if node.right:
            queue.append((node.right, lev+1))

    for i in range(maxLev+1):
        for j in range(len(hm[i])-1):
            f = hm[i][j]
            s = hm[i][j+1]
            f.next = s
            s.next = None
    
    return root