class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def calc(head):
    p = head
    l = 0

    while p:
        l += 1
        p = p.next

    return l

def reverse(head):
    p = head
    nxt = None
    prev = None

    while p:
        nxt = p.next
        p.next = prev

        prev = p
        p = nxt

    return prev

def getListAfterReverseOperation(head, n, b):
    dummy = Node(0)
    dummy.next = head

    p = dummy
    curr = None
    nxt = None

    length = calc(head)
    for i in range(n):
        if length == 0:
            break

        if b[i] <= length:
            curr = p.next
            nxt = curr.next

            if b[i] == 0:
                continue

            for j in range(b[i] - 1):
                curr.next = nxt.next
                nxt.next = p.next

                p.next = nxt
                nxt = curr.next

            length -= b[i]
            p = curr
        elif length <= b[i]:
            p.next = reverse(p.next)
            length = 0

    return dummy.next