def singleNonDuplicate(arr):
    curr, nxt = 0, 0
    while len(arr) >= 2:
        curr = arr.pop(0)
        nxt = arr.pop(0)
        if curr != nxt:
            return curr
        
    return arr[0]