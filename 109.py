def freq(s):
    hm = {}
    i = 0
    n = len(s)
    res = ""
    while i < n:
        if hm.get(s[i]):
            hm[s[i]] += 1
        else:
            hm[s[i]] = 1
        cur = i
        i += 1
        while i < n and s[cur] == s[i]:
            hm[s[cur]] += 1
            i += 1
        
        res += str(hm[s[cur]])
        res += str(s[cur])
        hm[s[cur]] = 0

    return res 

def writeAsYouSpeak(n):
    s = "1"
    if n == 1:
        return s
    for i in range(1, n):
        s = freq(s)
    
    return s