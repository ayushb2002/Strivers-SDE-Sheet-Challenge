def isValidColor(mat, color, i, c):
    for j in range(len(mat[i])):
        if mat[i][j] == 1 and color[j] == c:
            return False
    
    return True


def graphColoring(mat,m):
    n = len(mat)
    color = [-1]*n
    
    def backtrack(i):
        if -1 not in color:
            return True

        for c in range(m):
            if isValidColor(mat, color, i, c):
                color[i] = c
                if backtrack(i+1):
                    return True
                color[i] = -1
        return False

    res = backtrack(0)
    if res:
        return "YES"
    else:
        return "NO"