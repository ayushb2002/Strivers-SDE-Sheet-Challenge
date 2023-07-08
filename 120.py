def getMaxWidth(root):
    if not root:
        return 0
    queue = [(root, 0, 0)]
    hm = {}
    maxH = float('-inf')
    while queue:
        node, v, h = queue.pop(0)
        if node.left:
            queue.append((node.left, v-1, h+1))
        if node.right:
            queue.append((node.right, v+1, h+1))
        
        if hm.get(h):
            hm[h].append(node.val)
        else:
            hm[h] = [node.val]
        
        maxH = max(maxH, len(hm[h]))

    return maxH