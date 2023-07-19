import heapq

def kthLargest(arr, size, k):
    heap = []
    for i in arr:
        heapq.heappush(heap, -1*i)
    
    res = 0
    for _ in range(k):
        res = heapq.heappop(heap)

    return -1*res