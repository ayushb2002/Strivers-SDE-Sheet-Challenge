import heapq

class Stream:
    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    
    def addNum(self, num):
        heapq.heappush(self.small, -1*num) # for max heap
        if (self.small and self.large and (-1* self.small[0]) > self.large[0]):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
        
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)

    def getMedian(self):
        if len(self.small) > len(self.large):
            return -1*self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1*self.small[0] + self.large[0]) // 2


def findMedian(arr, n):
    res = []
    s = Stream()
    for i in range(n):
        s.addNum(arr[i])
        res.append(s.getMedian())
    
    return res