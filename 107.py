def minCharsforPalindrome(s):
    n = len(s)
    if n == 1:
        return 0
    t = s[::-1]
    dp = [[-1 for _ in range(n+1)] for __ in range(n+1)]
    
    def lcs(i, j):
        if i < 0 or j < 0:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        if s[i] == t[j]:
            dp[i][j] = 1+lcs(i-1, j-1)
        else:
            dp[i][j] = max(lcs(i-1, j), lcs(i, j-1))

        return dp[i][j]
    
    return n-lcs(n-1, n-1)