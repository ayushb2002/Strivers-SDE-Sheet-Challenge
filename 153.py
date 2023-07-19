from os import *
from sys import *
from collections import *
from math import *
import heapq
from sys import stdin 

class KthLargest:
    def __init__(self, k, nums):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
        self.latest = self.minHeap[0]
    
    def add(self, val):
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        self.latest = self.minHeap[0]
        return

    def getKthLargest(self):
        return self.latest
        
q,k = map(int,input().split(" "))

arr = list(map(int, stdin.readline().rstrip().split(" ")))

obj = KthLargest(k,arr)

for i in range(q):
    ip = list(map(int, stdin.readline().rstrip().split(" ")))

    # Ip[0] is 1 definitely.
    if len(ip) == 2: 

        # Add the value at ip[1] in the pool and sort it.
        obj.add(ip[1]) 

    # Means ip[0] is 2 definitely.    
    else:

        # Returns/prints the kth largest no.
        print(obj.getKthLargest())