def floydWarshall(n, m, src, dest, edges):
    dp = [[float('inf')]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0

    for u, v, w in edges:
        dp[u-1][v-1] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if k == i or k == j:
                    continue
                else:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    return 10**9 if dp[src-1][dest-1] == float('inf') else dp[src-1][dest-1]