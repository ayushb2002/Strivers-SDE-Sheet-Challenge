def firstNode(head):
    if not head:
        return head
    
    if not head.next:
        return None

    node = None
    first, second = head, head.next
    while first and second:
        if first and second and first == second:
            node = first
            break
        
        if first and first.next: 
            first=first.next
        else:
            first=None

        if second and second.next: 
            second=second.next
        else:
            second = None

        if second and second.next: 
            second=second.next
        else:
            second = None
    
    if not node:
        return node
    
    node = node.next
    ptr = head
    while ptr:
        if ptr == node:
            return ptr
        ptr = ptr.next
        node = node.next

    return None