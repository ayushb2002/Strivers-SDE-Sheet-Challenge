def removeDuplicates(arr,n):
    i, j = 0, 1
    if n == 1:
        return 1
    
    while j < n:
        if arr[i] == arr[j]:
            arr.pop(j)
            n -= 1
        else:
            i = j
            j += 1

    return n