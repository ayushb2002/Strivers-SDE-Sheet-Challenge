class Node:
    def __init__(self,data):
        
        self.data = data
        self.next = None
            
            
def isPalindrome(head):
    if not head:
        return True

    store = []
    while head:
        store.append(head.data)
        head = head.next
    
    return store == store[::-1]