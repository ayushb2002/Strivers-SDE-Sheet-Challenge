def subsetSum(num):

    res = []
    def dfs(i, s):
        if i >= len(num):
            res.append(s)
            return
        
        dfs(i+1, s+num[i])
        dfs(i+1, s)

    dfs(0, 0)

    return sorted(res)