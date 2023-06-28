class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.n = 0

    def getSize(self):
        return self.n

    def isEmpty(self):
        if self.n == 0:
            return "true"
        
        return "false"

    def push(self,ele):
        self.q2.append(ele)
        while len(self.q1) > 0:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1
        self.n += 1
        return

    def pop(self):
        if self.n <= 0:
            return -1
        
        self.n -= 1
        x = self.q1.pop(0)
        return x

    def top(self):
        if self.n <= 0:
            return -1

        return self.q1[0]