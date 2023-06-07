from os import *
from sys import *
from collections import *
from math import *

def nextPermutation(permutation, n):
    perm = permutation
    ind1, ind2 = 0, 0
    for i in range(n-1, 0, -1):
        if perm[i-1] < perm[i]:
            ind1 = i-1
            break
    for i in range(n-1, -1, -1):
        if perm[i] > perm[ind1]:
            ind2 = i
            break

    if ind1 == ind2:
        return perm[::-1]

    temp = perm[ind1]
    perm[ind1] = perm[ind2]
    perm[ind2] = temp

    x, y = perm[:ind1+1], perm[ind1+1:]
    y = y[::-1]
    perm = x+y

    return perm