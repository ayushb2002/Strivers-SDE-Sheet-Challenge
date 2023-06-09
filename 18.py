from sortedcontainers import SortedList

def reversePairs(arr, n):
    bst = SortedList()
    return sum([bst.add(k*2) or pairs for k in arr[::-1] for pairs in [bst.bisect_left(k)]])