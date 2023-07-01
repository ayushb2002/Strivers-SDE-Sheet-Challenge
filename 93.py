from collections import deque

def slidingWindowMaximum(nums, k):
    dq = deque()
    ans = []
    
    for i in range(len(nums)):
        # removing out of bound i.e out of window length index from deque
        if dq and dq[0] == i - k:
            dq.popleft()
        
        # removing all indexes from deque whose values are less than the current index value
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        
        # inserting the current at back of deque
        dq.append(i)
        
        # inserting the max element in ans list
        if i >= k - 1:
            ans.append(nums[dq[0]])
    
    return ans