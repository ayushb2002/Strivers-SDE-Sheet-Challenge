def original(arr):
    i, n = 0, len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            break
    rot = i+1
    while i >= 0:
        temp = arr[0]
        for j in range(1, n):
            arr[j-1] = arr[j]
        arr[n-1] = temp
        i -= 1

    return arr, rot

def search(arr, target) :
    org, rot = original(arr)
    l, r = 0, len(arr)-1

    res = -1
    while l <= r:
        m = l+ (r-l) // 2
        if org[m] == target:
            res = m
            break
        elif org[m] < target:
            l = m+1
        else:
            r = m-1

    if res == -1:
        return res
    
    if res+rot < len(arr):
        return res+rot
    else:
        return len(arr)-rot-res

queries = [1, -5, 4, 0, 3]
for q in queries:
    print(search([4, -1, 0, 2, 3], q))