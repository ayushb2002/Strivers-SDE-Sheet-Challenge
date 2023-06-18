def isValid(matrix, i, j, k):
    for x in range(9):
        if matrix[x][j] == k or matrix[i][x] == k:
            return False
    
    x_box, y_box = 3*(i // 3), 3*(j // 3)
    for x in range(x_box, x_box+3):
        for y in range(y_box, y_box+3):
            if matrix[x][y] == k:
                return False
    
    return True


def isItSudoku(matrix):
    for x in range(9):
        for y in range(9):
            if matrix[x][y] == 0:
                for k in range(1, 10):
                    if isValid(matrix, x, y, k):
                        matrix[x][y] = k
                        if isItSudoku(matrix):
                            return True
                        else:
                            matrix[x][y] = 0
                return False

    return True