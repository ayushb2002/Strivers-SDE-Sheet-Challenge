denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):

	res = 0
	i = 8
	while amount > 0:
		x = 1
		while denominations[i]*x <= amount:
			x += 1

		amount -= denominations[i]*(x-1)
		res += x-1
		i -= 1

	return res