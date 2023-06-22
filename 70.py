def kthSmallLarge(arr, n, k):
    arr.sort()
    res = []
    res.append(arr[k-1])
    arr = arr[::-1]
    res.append(arr[k-1])
    return res