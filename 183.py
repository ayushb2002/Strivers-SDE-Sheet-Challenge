def wordBreak(arr, n, target):

    dp = [[-1]*(len(target)+1) for _ in range(n)]

    def dfs(i, tar):
        if tar == "":
            return True

        if i < 0:
            return False

        if dp[i][len(tar)] != -1:
            return dp[i][len(tar)]
        
        nt = dfs(i-1, tar) if i-1 >= 0 else False
        t = (tar == arr[i])
        if not t and len(tar) >= len(arr[i]) and tar[:len(arr[i])] == arr[i]:
            t = dfs(n-1, tar[len(arr[i]):])
        
        dp[i][len(tar)] = (nt or t)
        return dp[i][len(tar)]
    
    return dfs(n-1, target)