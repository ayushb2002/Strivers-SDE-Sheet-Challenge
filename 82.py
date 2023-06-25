class Stack:
    
    def __init__(self, capacity: int):
        self.stack = []
        self.capacity = capacity
        self.n = 0

    def push(self, num: int) -> None:
        if self.n >= self.capacity:
            return
        
        self.stack.insert(0, num)
        self.n += 1

    def pop(self) -> int:
        if self.n == 0:
            return -1
        
        self.n -= 1
        return self.stack.pop(0)
    
    def top(self) -> int:
        if self.n == 0:
            return -1
        
        return self.stack[0]
    
    def isEmpty(self) -> int:
        if self.n == 0:
            return 1
        
        return 0
    
    def isFull(self) -> int:
        if self.n == self.capacity:
            return 1
        
        return 0
