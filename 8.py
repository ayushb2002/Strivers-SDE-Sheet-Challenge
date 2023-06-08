class Solution:
    def __init__ (self, start, end):
        self.start = start
        self.end = end

def mergeIntervals(intervals):
    store = []
    for inter in intervals:
        store.append((inter.start, inter.end))

    store.sort()
    res = []
    pair = store[0]

    for st in store:
        if pair[1] >= st[0] and pair[1] <= st[1]:
            pair = (pair[0], st[1])
        else:
            res.append(Solution(pair[0], pair[1]))
            pair = st
    
    res.append(Solution(pair[0], pair[1]))
    return res