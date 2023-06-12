class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findIntersection(f, s):
    d1, d2 = f, s
    m, n = 0, 0
    while d1 or d2:
        if d1:
            m += 1
            d1 = d1.next
        if d2:
            n += 1
            d2 = d2.next
    d1, d2 = f, s

    while m > n:
        d1 = d1.next
        m -= 1

    while n > m:
        d2 = d2.next
        n -= 1

    flag = 0
    store = d1
    while d1 and d2:
        if d1.data == d2.data:
            if not flag:
                flag = 1
                store = d1
        else:
            flag = 0

        d1 = d1.next
        d2 = d2.next

    return store if flag else Node(-1) 