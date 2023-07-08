import collections

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def verticalOrderTraversal(root):
    hm = {}
	
    queue = [(root, 0, 0)]
    while len(queue) > 0:
        node, v, h = queue.pop(0)
        if node.left:
            queue.append((node.left, v-1, h+1))
        if node.right:
            queue.append((node.right, v+1, h+1))
        
        if hm.get(v):
            if hm[v].get(h):
                hm[v][h].append(node.data)
            else:
                hm[v][h] = [node.data]
        else:
            hm[v] = {}
            hm[v][h] = [node.data]
    
    hm = collections.OrderedDict(sorted(hm.items()))
    res = []
    for k, v in hm.items():
        for k2, v2, in v.items():
            for i in v2:
                res.append(i)

    return res