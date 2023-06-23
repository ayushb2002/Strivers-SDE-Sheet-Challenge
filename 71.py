def kMaxSumCombination(a, b, n, k):
	a = sorted(a, reverse=True)
	b = sorted(b, reverse=True)
	c = []
	for i in a:
		for j in b:
			c.append(i+j)

	c = sorted(c, reverse=True)
	return c[:k]