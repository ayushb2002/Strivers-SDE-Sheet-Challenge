def rotateMatrix(mat, n, m):
    topleft = 0
    topright = m - 1
    bottomright = n - 1
    bottomleft = 0

    while topleft < topright and bottomleft < bottomright:
        temp = mat[topleft][bottomleft]
        for i in range(topleft + 1, bottomright + 1):
            mat[i - 1][bottomleft] = mat[i][bottomleft]
        for i in range(bottomleft + 1, topright + 1):
            mat[bottomright][i - 1] = mat[bottomright][i]
        for i in range(bottomright - 1, topleft - 1, -1):
            mat[i + 1][topright] = mat[i][topright]
        for i in range(topright - 1, bottomleft - 1, -1):
            mat[topleft][i + 1] = mat[topleft][i]
        mat[topleft][bottomleft + 1] = temp
        topleft += 1
        bottomleft += 1
        topright -= 1
        bottomright -= 1