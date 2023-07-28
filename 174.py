def maxProfit(values, weights, n, w):

    dp = [[-1]*(w+1) for _ in range(n)]
    def solve(i, we):
        if i == 0:
            if weights[0] <= we:
                return values[0]
            else:
                return 0

        if dp[i][we] != -1:
            return dp[i][we]

        nt = solve(i-1, we)
        t = float('-inf')
        if weights[i] <= we:
            t = values[i] + solve(i-1, we-weights[i])
        
        dp[i][we] = max(nt, t)
        return dp[i][we]
    
    return solve(n-1, w)