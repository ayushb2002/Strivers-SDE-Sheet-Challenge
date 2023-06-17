def isPal(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l+1, r-1
    return True

def partition(s):
    n = len(s)
    if n == 0:
        return [""]

    res = []
    cur = []
    def subs(i):
        if i >= n:
            res.append(cur.copy())
            return

        for j in range(i, n):
            if isPal(s, i, j):
                cur.append(s[i:j+1])
                subs(j+1)
                cur.pop()

    subs(0)
    return res