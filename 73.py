import heapq

def mergeKSortedArrays(kArrays, k:int):
	heap = []
	
	for arr in kArrays:
		heap += arr
		heapq.heapify(heap)

	n = len(heap)
	res = []
	while n > 0:
		n -= 1
		res.append(heapq.heappop(heap))

	return res