def reverseLinkedList(head):
    if not head:
        return head

    ptr1, ptr2 = head, head.next
    ptr1.next = None
    while ptr2:
        temp = ptr2.next
        ptr2.next = ptr1
        ptr1 = ptr2
        ptr2 = temp

    return ptr1