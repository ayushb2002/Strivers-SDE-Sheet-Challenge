class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def detectCycle(head) :
    if not head or not head.next:
        return False
    
    ptr1, ptr2 = head, head.next

    while ptr2 and ptr2.next:
        ptr1 = ptr1.next if ptr1 else None
        ptr2 = ptr2.next if ptr2 else None
        ptr2 = ptr2.next if ptr2 else None
        
        if ptr1 and ptr2 and ptr1 == ptr2:
            return True
        
    return False