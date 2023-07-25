def findIslands(mat, n, m):
	visited = [[0 for _ in range(m)] for _ in range(n)]
	count = 0
	moves = [(-1, 0), (-1, -1), (0, -1), (1, 0), (0, 1), (1, 1), (1, -1), (-1, 1)]
	def dfs(i, j):
		if visited[i][j]:
			return 

		visited[i][j] = 1
		for x, y in moves:
			_i = i + x
			_j = j + y
			if _i >= 0 and _i < n and _j >= 0 and _j < m and mat[_i][_j] == 1:
				dfs(_i, _j) 

	for i in range(n):
		for j in range(m):
			if not visited[i][j] and mat[i][j] == 1:
				count += 1
				dfs(i, j)

	return count