import math
import heapq

def getMedian(matrix):
    m = len(matrix)
    n = len(matrix[0])

    el = math.ceil(m*n/2)
    heap = []
    for i in range(m):
        heap.append((matrix[i][0], i, 0))
    
    heapq.heapify(heap)

    curr, i = 0, 0
    while el > 0:
        curr, i, j = heapq.heappop(heap)
        if j+1 < n:
            heapq.heappush(heap, (matrix[i][j+1], i, j+1))

        el -= 1
    
    return curr