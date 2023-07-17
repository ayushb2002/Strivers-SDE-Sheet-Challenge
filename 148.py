class BSTiterator:
    def __init__(self, root):
        self.stack = []
        self.n = 0
        while root:
            self.stack.insert(0, root)
            root = root.left
            self.n += 1

    def next(self):
        if self.n <= 0:
            return -1
        
        self.n -= 1
        ans = self.stack.pop(0)
        temp = ans.right
        while temp:
            self.stack.insert(0, temp)
            temp = temp.left
            self.n += 1
        
        return ans.data

    def hasNext(self):
        if self.n > 0:
            return True
        
        return False