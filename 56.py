import copy

def isSafeSpot(grid, i, j):
    m = len(grid)
    n = len(grid[0])

    if i < 0 or j < 0 or i >= m or j >= n:
        return False

    for x in range(m):
        if grid[x][j] == 1:
            return False
    
    for y in range(n):
        if grid[i][y] == 1:
            return False

    x, y = i, j
    while x >= 0 and y >= 0:
        if grid[x][y] == 1:
            return False
        
        x -= 1 
        y -= 1
    
    x, y = i, j

    while x < m and y < n:
        if grid[x][y] == 1:
            return False
        
        x += 1
        y += 1
    
    x, y = i, j

    while x >= 0 and y < n:
        if grid[x][y] == 1:
            return False
        
        x -= 1
        y += 1

    x, y = i, j

    while x < m and y >= 0:
        if grid[x][y] == 1:
            return False
        
        x += 1
        y -= 1

    return True
    
def solveNQueens(n):
    grid = [[0 for __ in range(n)] for _ in range(n)]

    def backtrack(count):
        if count == 0:
            return True
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 1 and isSafeSpot(grid, i, j):
                    grid[i][j] = 1
                    if backtrack(count-1):
                        return True
                    grid[i][j] = 0

        return False

    backtrack(n)
    return grid       

