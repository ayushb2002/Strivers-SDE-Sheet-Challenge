def findSpans(price):
    n = len(price)
    res = [1]*n
    stack = []

    for i in range(1, n):
        if price[i] < price[i-1]:
            stack.insert(0, (price[i-1], res[i-1]))
        elif price[i] == price[i-1]:
            res[i] += res[i-1]
            
        else:
            res[i] += res[i-1]
            while len(stack) > 0 and stack[0][0] <= price[i]:
                _, s = stack.pop(0)
                res[i] += s

    return res