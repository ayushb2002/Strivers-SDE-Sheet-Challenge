class minStack:
    # Constructor
    def __init__(self):
        self.stack = []
        self.n = 0
    
    # Function to add another element equal to num at the top of stack.
    def push(self, num: int) -> None:
        top, curr = self.stack[0] if self.n > 0 else (0, float('inf'))
        nex = num if num < curr else curr
        self.stack.insert(0, (num, nex))
        self.n += 1
        return 
    
    # Function to remove the top element of the stack.
    def pop(self) -> int:
        if self.n <= 0:
            return -1
        
        self.n -= 1
        top, curr = self.stack.pop(0)
        return top
    
    # Function to return the top element of stack if it is present. Otherwise return -1.
    def top(self) -> int:
        if self.n <= 0:
            return -1
        
        return self.stack[0][0]
    
    # Function to return minimum element of stack if it is present. Otherwise return -1.
    def getMin(self) -> int:
        if self.n <= 0:
            return -1

        return self.stack[0][1]