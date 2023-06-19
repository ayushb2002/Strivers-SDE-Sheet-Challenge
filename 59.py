def isValid(maze, i, j, n):
    if i >= 0 and j >=0 and i < n and j < n and maze[i][j] == 1:
        return True

    return False

def returnResult(path, n):
    mat = [[0]*n for _ in range(n)]
    for coor in path:
        x, y = coor
        mat[x][y] = 1
    
    res = []
    for row in mat:
        res += row
        
    return res

def ratInAMaze(maze, n):
    res = []
    path = [(0, 0)]
    moves = [(1, 0), (0, 1)]
    def backtrack(i, j):
        if i == n-1 and j == n-1:
            res.append(path.copy())
            return True
        
        for move in moves:
            x, y = move
            if isValid(maze, i+x, j+y, n):
                path.append((i+x, j+y))
                if backtrack(i+x, j+y):
                    return True
                path.pop()
        
        return False
    
    backtrack(0, 0)
    
    ans = []
    for p in res:
        t = returnResult(p, n)
        ans.append(t)
    
    return ans

maze = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print(ratInAMaze(maze, 3))