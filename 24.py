def uniqueSubstrings(inp) :
    n = len(inp)
    hm = {}
    ans = 0
    l, r = 0, 0

    while r < n:
        if inp[r] in hm:
            l = max(hm[inp[r]]+1, l)

        hm[inp[r]] = r
        ans = max(ans, r-l+1)
        r += 1

    return ans