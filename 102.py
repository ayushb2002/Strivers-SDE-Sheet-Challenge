def atoi(string):
    n = len(string)
    m = 1
    res = 0
    mp = {
        '1': 1, '4': 4, '7': 7, '0': 0,
        '2': 2, '5': 5, '8': 8,
        '3': 3, '6': 6, '9': 9
    }
    for i in range(n - 1, -1, -1):
        if string[i] not in mp:
            continue
        else:
            res += mp[string[i]] * m
            m *= 10
    
    if string[0] == '-':
        res *= -1

    return res

print(atoi('-lala12lala34'))