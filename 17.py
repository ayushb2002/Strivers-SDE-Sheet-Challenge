def uniquePaths(m, n):
	if m == 1 or n == 1:
		return 1

	dp = [[0 for _ in range(n+1)] for __ in range(m+1)] 
	dp[m-1][n-1] = 1

	for i in range(m-1, -1, -1):
		for j in range(n-1, -1, -1):
			dp[i][j] += dp[i+1][j] + dp[i][j+1]

	return dp[0][0]	