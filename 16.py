def majorityElementII(arr):
	bucket = {}
	n = len(arr) // 3

	for i in arr:
		if i in bucket:
			bucket[i] += 1
		else:
			bucket[i] = 1

	res = []

	for key, val in bucket.items():
		if val > n:
			res.append(key)

	return res