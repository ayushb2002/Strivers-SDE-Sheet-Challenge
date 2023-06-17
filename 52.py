def find(ind, target, arr, ans, ds):
    if target == 0:
        ans.append(ds.copy())
        return
    for i in range(ind, len(arr)):
        if i > ind and arr[i] == arr[i - 1]:
            continue
        if arr[i] > target:
            break
        ds.append(arr[i])
        find(i + 1, target - arr[i], arr, ans, ds)
        ds.pop()

def combinationSum2(arr, n, target):
    arr.sort()
    ans = []
    ds = []
    find(0, target, arr, ans, ds)
    return ans