import copy

def findSubsetsThatSumToK(arr, n, k) :
    res = []

    def subsets(i, s):
        if i >= n:
            if sum(s) == k:
                res.insert(0, copy.deepcopy(s))
            return
        
        s.append(arr[i])
        subsets(i+1, s)
        s.remove(arr[i])
        subsets(i+1, s)

    subsets(0, [])

    return res