def modularExponentiation(x, n, m):
	res = 1
	x = x%m
	if x == 0:
		return 0

	while n > 0:
		if (n&1) == 1:
			res = (res*x)%m

		n = n >> 1
		x = x**2 % m

	return res