def isPal(i, j, s):
    while i < j:
        if s[i] != s[j]:
            return False
        
        i += 1
        j -= 1

    return True

def palindromePartitioning(string):

    n = len(string)

    def dfs(i):
        if i == n:
            return 0

        minCost = float('inf')

        for j in range(i, n):
            if isPal(i, j, string):
                cost = 1+dfs(j+1)
                minCost = min(minCost, cost)

        return minCost
        
    res = dfs(0)
    if res in [1, 2]:
        return res-1
    
    return res-2