def pairSum(arr, s):
    res = []
    arr.sort()

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == s:
                res.append((arr[i], arr[j]))

    return res