def cutRod(price, n):
    dp = [[-1]*(n+1) for _ in range(n)]
    
    def dfs(i, m):        
        if i == 0:
            return m*price[0]

        if dp[i][m] != -1:
            return dp[i][m]

        nt = dfs(i-1, m)
        t = float('-inf')
        if m >= i+1:
            t = price[i]+dfs(i, m-(i+1))
        
        dp[i][m] = max(nt, t)
        return dp[i][m]

    return dfs(n-1, n)