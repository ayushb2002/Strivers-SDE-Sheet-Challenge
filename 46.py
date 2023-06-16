def maximumValue(items, n, w):

	ratio = []
	for i in range(n):
		try:
			ratio.append((items[i][0]/items[i][1], i))
		except:
			ratio.append((float('inf'), i))

	ratio.sort()

	res = 0
	for r, index in ratio:
		if w <= 0:
			break
		we, v = items[index]
		if we <= w:
			w -= we
			res += v
		else:
			res += round((v*(w/we)), 2)
			w = 0
	
	return res