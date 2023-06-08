def findDuplicate(arr:list, n:int):
    hashmap = {}

    for i in arr:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            return i

    return 0