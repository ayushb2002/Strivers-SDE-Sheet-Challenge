def countDistinctElements(arr, k):
    slide = arr[:k]
    res = [len(list(set(slide)))]
    i = k
    while i < len(arr):
        print(slide)
        slide.pop(0)
        slide.append(arr[i])
        res.append(len(list(set(slide))))
        i += 1

    return res        

print(countDistinctElements([1, 2, 1, 3, 4, 2, 3], 3))