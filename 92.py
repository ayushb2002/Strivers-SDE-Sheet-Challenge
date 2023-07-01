def leftBound(arr, n):
    left = [0]*n
    stack = []

    for i in range(n):
        while len(stack) > 0 and stack[0][1] > arr[i]:
            stack.pop(0)
        
        if len(stack) > 0:
            left[i] = stack[0][0]+1
        
        stack.insert(0, (i, arr[i]))
    
    #print(left)
    return left

def rightBound(arr, n):
    right = [n-1]*n
    stack = []

    for i in range(n-1, -1, -1):
        while len(stack) > 0 and stack[0][1] >= arr[i]:
            stack.pop(0)
        
        if len(stack) > 0:
            right[i] = stack[0][0]-1
        
        stack.insert(0, (i, arr[i]))

    #print(right)
    return right

def largestRectangle(arr):
    n = len(arr)
    left = leftBound(arr, n)
    right = rightBound(arr, n)
    area = [0]*n

    for i in range(n):
        area[i] = (right[i]-left[i]+1)*arr[i]

    return max(area)