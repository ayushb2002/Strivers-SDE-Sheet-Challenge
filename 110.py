def compareVersions(a, b):
    # splitting the string by '.' and mapping 'int' data type to
    # each element and converting them back to list
    a = list(map(int, a.split('.')))
    b = list(map(int, b.split('.')))

    # taking maximum length between two lists
    n = max(len(a), len(b))

    # looping through both lists simultaneously and comparing 2 values
    for i in range(n):
        num1 = a[i] if i < len(a) else 0
        num2 = b[i] if i < len(b) else 0
        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1

    # finally 0 is returned if both the strings are equal
    return 0