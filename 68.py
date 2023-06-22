def chessTournament(positions, n , c):
    positions.sort()
    ans = 0
    l, r = 1, positions[n-1]

    while l <= r:
        mid = (l+r) // 2

        count, last = 1, positions[0]
        for i in range(1, n):
            if positions[i] - last >= mid:
                count += 1
                last = positions[i]
        
        if count >= c:
            ans = mid
            l = mid+1
        else:
            r = mid-1

    return ans