def ayushGivesNinjatest(n, m, time):
    l, h = min(time), sum(time)
    while l <= h:
        mid = (l+h) // 2
        arr = [0]*n
        i, j = 0, 0
        flag = 0
        while j < m:
            if arr[i] + time[j] <= mid:
                arr[i] += time[j]
                j+=1
            else:
                i+=1
                if i >= n:
                    flag = 1 
                    break
        if flag == 1:
            l = mid+1
        elif not flag:
            h = mid-1

    return l