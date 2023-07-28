def matrixMultiplication(arr, n):
	dp = [[-1]*n for _ in range(n)]
	def dfs(i, j):
		if i == j:
			return 0

		if dp[i][j] != -1:
			return dp[i][j]

		mini = 1e9
		for k in range(i, j):
			steps = arr[i-1]*arr[k]*arr[j] + dfs(i, k) + dfs(k+1, j)
			mini = min(mini, steps)

		dp[i][j] = mini
		return dp[i][j]

	return dfs(1, n-1)