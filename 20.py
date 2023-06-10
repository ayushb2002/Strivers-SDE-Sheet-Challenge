def fourSum(arr, target):
    arr.sort()
    n = len(arr)
    if len(arr) < 4:
        return "No"

    flag = False
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            target_2 = target - arr[i]
            target_2 -= arr[j]

            k = j + 1
            l = len(arr) - 1

            while k < l:
                two_sum = arr[k] + arr[l]
                if two_sum > target_2:
                    l -= 1
                elif two_sum < target_2:
                    k += 1
                else:
                    flag = True
                    break

    return "Yes" if flag else "No"