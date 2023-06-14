class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child

def flattenLinkedList(head: Node) -> Node:
    if not head:
        return head
    if not head.next:
        return head
    
    res = Node(-1)
    temp = res
    ptr1, ptr2 = head, head.next
    head = ptr2.next

    while ptr1 and ptr2:
        if ptr1.data < ptr2.data:
            temp.child = ptr1
            temp = temp.child
            ptr1 = ptr1.child
        else:
            temp.child = ptr2
            temp = temp.child
            ptr2 = ptr2.child
        
    while ptr1:
        temp.child = ptr1
        temp = temp.child
        ptr1 = ptr1.child
        
    while ptr2:
        temp.child = ptr2
        temp = temp.child
        ptr2 = ptr2.child

    while head:
        newRes = Node(-1)
        temp = newRes
        ptr1, ptr2 = res, head

        while ptr1 and ptr2:
            if ptr1.data < ptr2.data:
                temp.child = ptr1
                temp = temp.child
                ptr1 = ptr1.child
            else:
                temp.child = ptr2
                temp = temp.child
                ptr2 = ptr2.child
        
        while ptr1:
            temp.child = ptr1
            temp = temp.child
            ptr1 = ptr1.child
        
        while ptr2:
            temp.child = ptr2
            temp = temp.child
            ptr2 = ptr2.child

        head = head.next
        res = newRes.child

    return res.child