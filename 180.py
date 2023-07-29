def subsetSumToK(n, k, arr):

    dp = [[-1]*(k+1) for _ in range(n)]

    def dfs(i, tar):
        if tar == 0:
            return True
        
        if i == 0:
            return tar == arr[0]
        
        if dp[i][tar] != -1:
            return dp[i][tar]
        
        nt = dfs(i-1, tar)
        t = False
        if tar >= arr[i]:
            t = dfs(i-1, tar-arr[i])

        dp[i][tar] = (t or nt)
        return dp[i][tar]

    return dfs(n-1, k)