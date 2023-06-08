def searchMatrix(mat, target):
    m = len(mat)
    n = len(mat[0])

    i = 0
    while i < m:
        if target <= mat[i][n-1]:
            break
        i += 1
    
    if i >= m:
        return False

    j = 0
    while j < n:
        if target == mat[i][j]:
            break
        j += 1
    
    if j < n:
        return True
    
    return False