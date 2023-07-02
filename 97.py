from sys import maxsize

def previousSmaller(arr, n):

    prev = []

    s = []

    for i in range(n):

        while (len(s) != 0 and arr[s[-1]] >= arr[i]):

            s.pop()

        if (len(s) == 0):

            prev.append(-1)

        else:

            prev.append(s[-1])

        s.append(i)

    return prev

 
def nextSmaller(arr, n):
    s = []

    next = [0] * n

    for i in range(n-1, -1, -1):

        while (len(s) != 0 and arr[s[-1]] >= arr[i]):

            s.pop()

        if (len(s) == 0):

            next[i] = n

        else:

            next[i] = s[-1]

        s.append(i)

    return next

def maxMinWindow(arr, n):
    INT_MIN = -maxsize - 1

    answer = [INT_MIN] * n

    next = nextSmaller(arr, n)

    prev = previousSmaller(arr, n)

    for i in range(n):

        length = next[i] - prev[i] - 1

        answer[length - 1] = max(answer[length - 1], arr[i])

    for i in range(n - 2, -1, -1):
        answer[i] = max(answer[i], answer[i + 1])

    return answer