class Heap:
    def __init__(self):
        self.heap = []
        self.n = 0

    def heapPush(self, val):
        if self.n == 0:
            self.heap.append(val)
            self.n += 1
            return
        
        self.heap.append(val)
        self.n += 1
        cur, par = self.n-1, -1
        while cur > 0:
            par = cur // 2
            if self.heap[cur] < self.heap[par]:
                self.heap[cur], self.heap[par] = self.heap[par], self.heap[cur]
                cur = par
            else:
                break
        return
    
    def heapPop(self):
        if self.n == 0:
            return
        
        self.heap[self.n-1], self.heap[0] = self.heap[0], self.heap[self.n-1]
        x = self.heap.pop()
        self.n -= 1
        cur, l, r = 0, -1, -1
        while True:
            l, r = cur*2+1 if cur*2+1 < self.n else -1, cur*2+2 if cur*2+2 < self.n else -1
            
            if l == -1:
                break
            elif r == -1:
                if self.heap[cur] <= self.heap[l]:
                    break
                else:
                    self.heap[cur], self.heap[l] = self.heap[l], self.heap[cur]
                    cur = l
            else:
                if self.heap[cur] <= self.heap[l] and self.heap[cur] <= self.heap[r]:
                    break
                else:
                    sm = l if self.heap[l] < self.heap[r] else r
                    if self.heap[cur] > self.heap[sm]:
                        self.heap[cur], self.heap[sm] = self.heap[sm], self.heap[cur]
                        cur = sm
                    else:
                        newSm = l if sm == r else r
                        self.heap[cur], self.heap[newSm] = self.heap[newSm], self.heap[cur]
                        cur = newSm
        
        return x
    
heap = Heap()
heap.heapPush(32)
x = heap.heapPop()
print(x)
heap.heapPush(30)
heap.heapPush(48)
heap.heapPush(13)
x = heap.heapPop()
print(x)
heap.heapPush(10)
x = heap.heapPop()
print(x)
heap.heapPush(8)
heap.heapPush(38)