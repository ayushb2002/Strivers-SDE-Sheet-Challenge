from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    l, r = 0, 1
    res = 0
    while r < len(prices):
        if prices[r]-prices[l] < 0:
            l = r
            r = r+1
        else:
            res = max(res, prices[r]-prices[l])
            r += 1
    
    return res