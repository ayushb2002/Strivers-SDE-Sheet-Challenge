def romanToInt(s:str):
    hm = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = 0
    n = len(s)

    for i in range(n):
        if i+1<n and hm[s[i]] < hm[s[i+1]]:
            res -= hm[s[i]]
        else:
            res += hm[s[i]]

    return res

print(romanToInt('LXXIX'))