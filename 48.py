def maximumActivities(start, finish):
    jobs = []
    n = len(start)
    for i in range(n):
        jobs.append((start[i], finish[i]))

    jobs = sorted(jobs, key=lambda x:x[1])
    res = 1
    last = jobs[0][1]

    for i in range(1, n):
        if jobs[i][0] >= last:
            res += 1
            last = jobs[i][1]

    return res