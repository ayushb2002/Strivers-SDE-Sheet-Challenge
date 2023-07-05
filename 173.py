def lcs(s, t) :
	m, n = len(s), len(t)
	dp = [[-1]*m]*n

	def rec(i, j):
		if i < 0 or j < 0:
			return 0

		if dp[i][j] != -1:
			return dp[i][j]

		if s[i] == t[j]:
			dp[i][j] = 1+rec(i-1, j-1)
			return dp[i][j]
		
		dp[i][j] = max(rec(i-1, j), rec(i, j-1))
		return dp[i][j]
	
	return rec(m-1, n-1)

s = "abcdb"
t = "bcacdhb"
print(lcs(s, t))