from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :
    bucket = {0:0, 1:0, 2:0}
    for i in arr:
        bucket[i] += 1

    bucket[1] += bucket[0]
    bucket[2] += bucket[1]

    for i in range(n):
        if i < bucket[0]:
            arr[i] = 0
        elif i < bucket[1]:
            arr[i] = 1
        else:
            arr[i] = 2

    return arr


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
