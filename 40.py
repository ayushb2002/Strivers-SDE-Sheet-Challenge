def getTrappedWater(arr, n) :
	if n <= 2:
		return 0
	
	left, right = [0]*n, [0]*n
	left[0] = arr[0]
	right[n-1] = arr[n-1]
	for i in range(1, n):
		left[i] = max(arr[i], left[i-1])
	
	for i in range(n-2, -1, -1):
		right[i] = max(arr[i], right[i+1])
		
	res = 0
	for i in range(n):
		amt = min(left[i], right[i]) - arr[i]
		if amt > 0:
			res += amt
	
	return res