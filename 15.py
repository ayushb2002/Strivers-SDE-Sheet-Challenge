def findMajorityElement(arr, n):
	bucket = {}
	for i in arr:
		if i in bucket:
			bucket[i] += 1
		else:
			bucket[i] = 1

	maxEl = max(bucket, key=lambda k:bucket[k] )
	if bucket[maxEl] > (n // 2):
		return maxEl

	return -1