def LongestSubsetWithZeroSum(arr):

    hm = {}
    ans = 0

    for i in range(len(arr)):
        sm = sum(arr[:i+1])
        if sm == 0:
            ans = max(ans, i+1)
        else:
            if sm in hm:
                ans = max(ans, i-hm[sm])
            else:
                hm[sm] = i

    return ans