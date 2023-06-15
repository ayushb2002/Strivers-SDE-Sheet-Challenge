def longestSubSeg(arr, n, k):
    if n == 1:
        if arr[0] == 1:
            return 1
        else:
            return 0
    
    l, r = 0, 0
    cnt = 0 
    res = 0

    while r < n:
        if arr[r] == 0:
            cnt += 1
        
        while cnt > k:
            if arr[l] == 0:
                cnt -= 1
            l += 1
        
        res = max(res, r-l+1)
        r += 1
    
    return res