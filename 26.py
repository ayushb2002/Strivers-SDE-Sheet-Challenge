def findMiddle(head):
    if not head:
        return head
    
    n = 0
    node = head
    while node:
        n += 1
        node = node.next

    n = n//2
    if n <= 1:
        return head
    
    node = head
    while n>0:
        n -= 1
        node = node.next

    return node