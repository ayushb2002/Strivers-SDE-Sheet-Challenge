class Queue :

    #Define data members and __init__()
    def __init__(self):
        self.queue = []
        self.n = 0

    '''----------------- Public Functions of Queue -----------------'''

   
    def isEmpty(self) :
        if self.n == 0:
            return True
        return False


    def enqueue(self, data) :
        self.queue.append(data)
        self.n += 1

    def dequeue(self) :
        if self.n == 0:
            return -1
        
        self.n -= 1
        return self.queue.pop(0)

    def front(self) :
        if self.n == 0:
            return -1
        
        return self.queue[0]