def calculateMinPatforms(at, dt, n):
    at.sort()
    dt.sort()

    i, j = 0, 0
    curr, res = 0, 0

    while i < n and j < n:
        if at[i] <= dt[j]:
            curr += 1
            i += 1
        elif at[i] > dt[j]:
            curr -= 1
            j += 1
        
        res = max(res, curr)

    return res