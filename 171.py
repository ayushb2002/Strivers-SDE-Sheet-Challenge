def maximumProduct(arr, n):
    res = float('-inf')
    pref, suff = 1, 1

    for i in range(n):
        if pref == 0:
            pref = 1
        if suff == 0:
            suff = 1
        
        pref *= arr[i]
        suff *= arr[n-i-1]

        res = max(res, max(pref, suff))
    
    return res
