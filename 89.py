def nextSmallerElement(arr,n):
    res = [-1]*n
    stack = []
    for i in range(n-1, -1, -1):
        while len(stack) > 0:
            if stack[0] < arr[i]:
                res[i] = stack[0]
                break
            else:
                stack.pop(0)

        stack.insert(0, arr[i])
    
    return res