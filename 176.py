def maxIncreasingDumbbellsSum(rack, n):

    dp = [[-1]*n for _ in range(n)]

    def dfs(i, prev):
        if i >= n:
            return 0

        if dp[i][prev] != -1:
            return dp[i][prev]

        nt = dfs(i+1, prev)
        t = float('-inf')
        
        if prev == -1 or rack[i] > rack[prev]:
            t = rack[i]+dfs(i+1, i)

        dp[i][prev] = max(nt, t)
        return dp[i][prev]

    return dfs(0, -1)