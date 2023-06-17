def factorial(n):
    if n == 1 or n == 0:
        return n
    
    return n*factorial(n-1)

def kthPermutation(n, k):
    nums = [i for i in range(1, n+1)]

    k -= 1
    res = []
    n = len(nums)
    while n > 0:
        fc = factorial(n-1)
        if fc == 0:
            res.append(str(nums[0]))
            break
        pos = k // fc
        k = k % fc
        res.append(str(nums[pos]))
        nums.pop(pos)
        n -= 1

    s = ''.join(res)
    return s
