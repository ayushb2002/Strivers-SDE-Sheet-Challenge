def stringMatch(s, pat):
    res = []
    m = len(s)
    n = len(pat)
    h = 26
    hs, hpat = 0, 0
    for i in range(n):
        hpat += (ord(pat[i]) - ord('a'))*(h**(n-i-1))
        hs += (ord(s[i]) - ord('a'))*(h**(n-i-1))

    if hs == hpat:
        res.append(1)

    for i in range(n, m):
        hs -= (ord(s[i-n]) - ord('a'))*(h**(n-1))
        hs *= h
        hs += (ord(s[i]) - ord('a'))
        if hs == hpat:
            res.append(i-n+2)
    
    return res if res != [] else -1

s = "nrolbdiagrfsnafxlrgujdyngkwkihmllcjimuwl"
pat = "jdyngkwkihmllcjimuwl"


print(stringMatch(s, pat))