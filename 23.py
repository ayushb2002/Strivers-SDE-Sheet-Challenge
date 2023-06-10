def subarraysXor(arr, x):
    n = len(arr)
    xor = 0
    count = 0
    hm = {}

    for i in range(n):
        xor = xor^arr[i]
        if xor == x:
            count += 1
        
        y = xor^x
        if y in hm:
            count += hm[y] 
            
        if xor not in hm:
            hm[xor] = 0

        hm[xor] += 1
        
    return count