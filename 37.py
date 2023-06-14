class Node:
    def __init__(self, val, next=None):
        self.data = val
        self.next = next

def listLen(head):
    c = 0
    while head:
        c += 1
        head = head.next

    return c

def rotate(head: Node, k: int) -> Node:
    if not head:
        return head

    if k == 0:
        return head

    n = listLen(head)
    k %= n
    n -= k
    ptr1 = head
    while n > 1:
        ptr1 = ptr1.next
        n -= 1
    
    ptr2 = ptr1

    while ptr1.next is not None:
        ptr1 = ptr1.next

    ptr1.next = head
    newHead = ptr2.next
    ptr2.next = None
    return newHead