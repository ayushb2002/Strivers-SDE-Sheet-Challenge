import copy

def pwset(v):
    ps = []
    n = len(v)
    curr = []
    def subsets(i):
        if i >= n:
            ps.append(copy.deepcopy(curr))
            return

        curr.append(v[i])
        subsets(i+1)
        curr.pop()
        subsets(i+1)
    
    subsets(0)

    return ps