def pow(a, n):
    r = 1.0
    for _ in range(1, n+1):
        r *= a
    
    return r

def NthRoot(n: int, m: int) -> int:
    low, high = 1, m
    eps = 1e-7

    while (high-low) > eps:
        mid = (low+high) / 2.0
        if pow(mid, n) < m:
            low = mid
        else:
            high = mid

    return low

print(NthRoot(3, 27))