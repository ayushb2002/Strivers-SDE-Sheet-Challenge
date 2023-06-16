def jobScheduling(jobs):
    max_d = 0

    for d, p in jobs:
        if max_d < d:
            max_d = d

    schedule = [-1]*max_d
    jobs = sorted(jobs, key=lambda x:x[1], reverse=True)
    
    for d, p in jobs:
        if schedule[d-1] == -1:
            schedule[d-1] = p
        else:
            while d > 0:
                if schedule[d-1] == -1:
                    schedule[d-1] = p
                    break
                d -= 1
    
    res = 0
    for i in schedule:
        if i != -1:
            res += i

    return res