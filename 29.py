class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def addTwoNumbers(head1: Node, head2: Node) -> Node:

    num1, num2 = [], []
    while head1:
        num1.append(head1.data)
        head1 = head1.next
    
    while head2:
        num2.append(head2.data)
        head2 = head2.next

    m, n = len(num1), len(num2)
    resList = []
    i, j, c = 0, 0, 0
    while i < m and j < n:
        c += num1[i]+num2[j]
        i += 1
        j += 1
        resList.append(c%10)
        c //= 10
    
    while i < m:
        c += num1[i]
        i += 1
        resList.append(c%10)
        c //= 10
    
    while j < n:
        c += num2[j]
        j += 1
        resList.append(c%10)
        c //= 10

    if c > 0:
        resList.append(c)
    
    head = Node(resList[0])
    if len(resList) == 1:
        return head
    node = head
    for i in resList[1:]:
        node.next = Node(i)
        node = node.next

    return head 