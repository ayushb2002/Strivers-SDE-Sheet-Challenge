from bisect import bisect_left

def longestIncreasingSubsequence(arr, n):
    dp = []
    ans = 1
    dp.append(arr[0])
    for i in range(1, n):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            ind = bisect_left(dp, arr[i])
            dp[ind] = arr[i]
    return len(dp)