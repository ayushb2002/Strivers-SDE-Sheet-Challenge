def ninjaAndSortedArrays(arr1,arr2,m,n):
    i = m-1
    j = n-1
    k = m+n-1

    while k >= 0:
        if i >= 0 and j >= 0:
            if arr1[i] > arr2[j]:
                arr1[k] = arr1[i]
                k -= 1
                i -= 1
            else:
                arr1[k] = arr2[j]
                k -= 1
                j -= 1
        elif i >= 0:
            arr1[k] = arr1[i]
            k -= 1
            i -= 1
        elif j >= 0:
            arr1[k] = arr2[j]
            k -= 1
            j -= 1
            
    return arr1