def twoSum(arr, k):
    l, r = 0, len(arr)-1
    while l < r:
        if arr[l]+arr[r] == k:
            break
        elif arr[l]+arr[r] > k:
            r -= 1
        else:
            l += 1
    
    return (arr[l]+arr[r]) == k

def pairSumBST(root, k):
    store = []

    def inorder(root):
        if not root:
            return

        inorder(root.left)
        store.append(root.data)
        inorder(root.right)
    
    inorder(root)
    return twoSum(store, k)