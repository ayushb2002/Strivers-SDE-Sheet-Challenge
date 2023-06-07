from os import *
from sys import *
from collections import *
from math import *
import copy

def printPascal(n:int):
    result = []
    for i in range(n):
        row = [None] * (i + 1)
        row[0] = 1
        row[i] = 1
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    return result