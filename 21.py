def lengthOfLongestConsecutiveSequence(arr, n):
    if len(arr) <= 1:
        return 1
    arr = list(set(arr))
    arr.sort()
    r = 1
    maxRes = 1
    res = 1
    while r<len(arr):
        while r<len(arr) and arr[r]-arr[r-1] == 1:
            res += 1
            r += 1

        maxRes = max(maxRes, res)
        res = 1
        r += 1
    
    return maxRes