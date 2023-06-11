def removeKthNode(head, k):
    if not head:
        return head

    node = head
    n = 0
    while node:
        n += 1
        node = node.next

    if n == k:
        return head.next

    n -= k
    node = head
    while n > 1:
        n -= 1
        node = node.next
    
    temp = node.next
    node.next = temp.next
    del temp

    return head