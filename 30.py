class LinkedListNode:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next

def deleteNode(node):
    ptr = node.next
    node.data = ptr.data
    node.next = ptr.next
    del ptr