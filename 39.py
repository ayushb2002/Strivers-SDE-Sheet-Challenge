def findTriplets(arr, n, k):
    arr.sort()
    s = set()
    ans = []

    for i in range(n - 2):
        low = i + 1
        high = n - 1

        while low < high:
            if arr[i] + arr[low] + arr[high] < k:
                low += 1
            elif arr[i] + arr[low] + arr[high] > k:
                high -= 1
            else:
                s.add((arr[i], arr[low], arr[high]))
                low += 1
                high -= 1

    for a in s:
        ans.append(list(a))

    return ans