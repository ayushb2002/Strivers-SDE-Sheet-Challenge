import copy

def uniqueSubsets(n ,arr):
    arr.sort()
    res = []
    def subsets(i, nums):
        if i >= n:
            if nums not in res:
                res.insert(0, copy.deepcopy(nums))
            return 
        
        nums.append(arr[i])
        subsets(i+1, nums)
        nums.remove(arr[i])
        subsets(i+1, nums)

    subsets(0, [])

    return res