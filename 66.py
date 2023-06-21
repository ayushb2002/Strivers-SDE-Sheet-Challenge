def ninjaAndLadoos(row1, row2, m, n, k):
    if m > n:
        return ninjaAndLadoos(row2, row1, n, m, k)

    l, h = max(0, k-m), min(k, n)

    while l <= h:
        c1 = (l+h) // 2
        c2 = k - c1

        l1 = float('-inf') if c1 == 0 else row1[c1-1]
        l2 = float('-inf') if c2 == 0 else row2[c2-1]
        r1 = float('inf') if c1 == m else row1[c1]
        r2 = float('inf') if c2 == n else row2[c2]

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            h = c1-1
        else:
            l = c1+1
        
    return 1
    