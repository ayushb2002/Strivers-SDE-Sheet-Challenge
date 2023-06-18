def findPermutations(s):
	arr = [i for i in s]
	res = []
	n = len(arr)
	visit = [0]*n

	def dfs(visit, store):
		if len(store) == len(visit):
			res.append(store.copy())
			return

		for i in range(n):
			if not visit[i]:
				store.append(s[i])
				visit[i] = 1
				dfs(visit, store)
				visit[i] = 0
				store.pop()


	dfs(visit, [])
	ans = []
	for r in res:
		ans.append(''.join(r))

	return ans