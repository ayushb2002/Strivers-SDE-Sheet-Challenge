class LRUCache:
    class Node:
        def __init__(self, key, data):
            self.key = key
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        self.cap = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}

    def delete_node(self, temp):
        p = temp.prev
        n = temp.next
        p.next = n
        n.prev = p

    def add_node(self, temp):
        p = self.head.next
        self.head.next = temp
        temp.next = p
        p.prev = temp
        temp.prev = self.head

    def get(self, key):
        if key in self.m:
            temp = self.m[key]
            vl = temp.data
            del self.m[key]
            self.delete_node(temp)
            self.add_node(temp)
            self.m[key] = self.head.next
            return vl
        return -1

    def put(self, key, value):
        if key in self.m:
            temp = self.m[key]
            del self.m[key]
            self.delete_node(temp)
        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.delete_node(self.tail.prev)
        new_node = self.Node(key, value)
        self.add_node(new_node)
        self.m[key] = self.head.next
