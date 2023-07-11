def isSymmetric(root) :
    if not root:
        return True
    
    r1 = root.left 
    r2 = root.right

    def trav(r1, r2):
        if not r1 or not r2:
            return r1 == r2
        
        if r1.data != r2.data:
            return False

        return (trav(r1.left, r2.right) and trav(r1.right, r2.left))
    
    return trav(r1, r2)