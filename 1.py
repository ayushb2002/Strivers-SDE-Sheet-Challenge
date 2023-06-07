from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])
    
    rows = set()
    cols = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    
    rows = list(rows)
    cols = list(cols)

    for r in rows:
        for j in range(n):
            matrix[r][j] = 0
    
    for c in cols:
        for i in range(m):
            matrix[i][c] = 0