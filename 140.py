def inorder(root,arr):

    if root:

        inorder(root.left,arr)

        arr.append(root.data)

        inorder(root.right,arr)

    

 

        

def validateBST(root):

    arr=[]

    inorder(root,arr)

    for i in range(1,len(arr)):

        if arr[i-1]>arr[i]:

            return False

    return True