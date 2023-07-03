def longestCommonPrefix(arr, n):
    res = ""
    for i in range(len(arr[0])):
        for j in range(n):
            if i == len(arr[j]) or arr[j][i] != arr[0][i]:
                return res
        res += arr[0][i]

    return res
