def nextGreater(arr,n):
    res = []
    stack = []
    for i in range(n-1, -1, -1):
        flag = 0
        while len(stack) > 0:
            if stack[0] > arr[i]:
                res.insert(0, stack[0])
                flag = 1
                break
            else:
                stack.pop(0)
            
        if not flag:
            res.insert(0, -1)
        
        stack.insert(0, arr[i])
    
    return res