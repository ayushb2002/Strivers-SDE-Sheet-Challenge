class TreeNode:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def depth(root):
    if not root:
        return 0
    
    l = depth(root.left)
    r = depth(root.right)
    
    return 1+max(l, r)

def serializeTree(root):
    if not root:
        return "-1"
    
    n = depth(root)
    queue = [(root, 1)]
    res = ""
    while len(queue) > 0:
        node, lev = queue.pop(0)
        if lev > n:
            break
        
        if node:
            res += str(node.data)
            res += ','
            if node.left:
                queue.append((node.left, lev+1))
            else:
                queue.append((None, lev+1))
            
            if node.right:
                queue.append((node.right, lev+1))
            else:
                queue.append((None, lev+1))
        else:
            res += "-1,"
            queue.append((None, lev+1))
            queue.append((None, lev+1))
    
    return res[:len(res)-1]


def deserializeTree(serialized):
    if serialized == "-1":
        return None
        
    data = serialized.split(',')
    data = [int(i) for i in data]
    n = len(data)
    def buildTree(i):
        if i >= n or data[i] == -1:
            return None

        root = TreeNode(data[i])
        root.left = buildTree(2*i+1)
        root.right = buildTree(2*i+2)
        return root
    
    root = buildTree(0)

    return root