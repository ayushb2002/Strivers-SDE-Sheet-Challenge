from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def countWaysToMakeChange(denominations, value) :
    n = len(denominations)
    dp = [[-1]*(value+1) for _ in range(n)]
    def dfs(i, tar):
        if i == 0:
            return (tar % denominations[0]) == 0

        if dp[i][tar] != -1:
            return dp[i][tar]

        nt = dfs(i-1, tar)
        t = 0
        if denominations[i] <= tar:
            t = dfs(i, tar-denominations[i])
            
        dp[i][tar] = nt + t
        return dp[i][tar]
    
    return dfs(n-1, value)