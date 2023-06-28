class Queue:

    def __init__(self):
        self.s1 = []
        self.n = 0

    def enQueue(self, val):
        s2 = []
        while len(self.s1) > 0:
            s2.append(self.s1.pop())
        
        self.s1.append(val)
        self.n += 1
        while len(s2) > 0:
            self.s1.append(s2.pop())

    def deQueue(self):
        if self.n <= 0:
            return -1
        
        self.n -= 1
        return self.s1.pop()

    def peek(self):
        if self.n <= 0:
            return -1
            
        return self.s1[self.n-1]

    def isEmpty(self):
        if self.n == 0:
            return "true"
        
        return "false"