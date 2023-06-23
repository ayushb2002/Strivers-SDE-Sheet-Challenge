import heapq

def maxPush(heap, val):
    heapq.heappush(heap, -1*val)

def maxpop(heap):
    return -1*heapq.heappop(heap)

def findMedian(arr, n):
    if n <= 1:
        return arr

    maxheap = [-1*arr[0]]
    minheap = []
    res = [arr[0]]

    for i in range(1, n):
        if arr[i] > -1*maxheap[0]:
            heapq.heappush(minheap, arr[i])
        else:
            maxPush(maxheap, arr[i])
        
        if len(minheap) > len(maxheap):
            top = heapq.heappop(minheap)
            maxPush(maxheap, top)
        elif len(minheap)+1 < len(maxheap):
            top = maxpop(maxheap)
            heapq.heappush(minheap, top)

        if (i+1)%2 == 0:
            res.append((-1*maxheap[0]+minheap[0])//2)
        else:
            res.append(-1*maxheap[0])

    for i in res:
        print(i, end=' ')