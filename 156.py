def floodFill(image, x, y, newColor):
    m, n = len(image[0]), len(image)
    target = image[x][y]
    visited = [[0]*m for _ in range(n)]
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    def dfs(i, j):
        if i >= n or j >= m or i < 0 or j < 0:
            return

        if visited[i][j]:
            return

        visited[i][j] = 1
        image[i][j] = newColor

        for move in moves:
            new_i = i + move[0]
            new_j = j + move[1]
            if new_i >= n or new_j >= m or new_i < 0 or new_j < 0 or visited[new_i][new_j]:
                continue

            elif target == image[new_i][new_j]:
                dfs(new_i, new_j)

    dfs(x, y)
    return image