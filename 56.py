def solve(ans, col, n, board, leftrow, lowerdig, upperdig):
    if col == n:
        temp = []
        for i in range(n):
            for j in range(n):
                temp.append(board[i][j])
        ans.append(temp)
        return
    
    for row in range(n):
        if leftrow[row] == 0 and lowerdig[row + col] == 0 and upperdig[n - 1 + col - row] == 0:
            board[row][col] = 1
            leftrow[row] = 1
            lowerdig[row + col] = 1
            upperdig[n - 1 + col - row] = 1
            solve(ans, col + 1, n, board, leftrow, lowerdig, upperdig)
            board[row][col] = 0
            leftrow[row] = 0
            lowerdig[row + col] = 0
            upperdig[n - 1 + col - row] = 0


def solveNQueens(n):
    ans = []
    board = [[0] * n for _ in range(n)]
    leftrow = [0] * n
    lowerdig = [0] * (2 * n - 1)
    upperdig = [0] * (2 * n - 1)

    solve(ans, 0, n, board, leftrow, lowerdig, upperdig)

    return ans