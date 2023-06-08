def missingAndRepeating(arr, n):
    hashmap = {}
    for i in range(1, n+1):
        hashmap[i] = 0

    for i in arr:
        hashmap[i] += 1

    revmap = {v:k for k,v in hashmap.items()}

    return (revmap[0], revmap[2])