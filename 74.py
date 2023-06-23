import heapq
from typing import List


def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
    hm = {}

    for i in arr:
        if i in hm:
            hm[i] += 1
        else:
            hm[i] = 1

    hm_list = [(-val, key) for key, val in hm.items()]
    heapq.heapify(hm_list)
    res = []
    for i in range(k):
        f, v = heapq.heappop(hm_list)
        res.append(v)

    return sorted(res)