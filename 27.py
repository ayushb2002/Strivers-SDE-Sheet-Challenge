class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sortTwoLists(first, second):
    if not first and not second:
        return None
    if not first:
        return second
    if not second:
        return first
    
    ptr1, ptr2 = first, second

    while ptr1 and ptr2:
        if ptr1.data < ptr2.data:
            ptr1 = ptr1.next
        else:
            ptr1.data, ptr2.data = ptr2.data, ptr1.data
            t1, t2 = ptr1.next, ptr2.next
            ptr1.next = ptr2
            ptr2.next = t1
            ptr1 = ptr1.next
            ptr2 = t2
    
    node = first
    while node.next:
        node = node.next

    node.next = ptr2

    return first