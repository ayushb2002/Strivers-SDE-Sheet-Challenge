class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class List:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNewNode(self, newNode):
        temp = self.head.next
        newNode.next = temp
        newNode.prev = self.head
        self.head.next = newNode
        temp.prev = newNode
        self.size += 1

    def deleteNode(self, delNode):
        delNode.next.prev = delNode.prev
        delNode.prev.next = delNode.next
        self.size -= 1


class LFUCache:
    def __init__(self, capacity):
        self.mp = {}  # key: int -> Node
        self.freqList = {}  # freq: int -> List
        self.minFreq = 0
        self.cap = capacity
        self.currSize = 0

    def updateList(self, node):
        del self.mp[node.key]
        self.freqList[node.freq].deleteNode(node)

        if self.freqList[node.freq].size == 0 or node.freq == self.minFreq:
            self.minFreq += 1

        new_list = List()
        if node.freq + 1 in self.freqList:
            new_list = self.freqList[node.freq + 1]

        node.freq += 1
        new_list.addNewNode(node)
        self.freqList[node.freq] = new_list
        self.mp[node.key] = node

    def get(self, key):
        if key in self.mp:
            node = self.mp[key]
            x = node.val
            self.updateList(node)
            return x
        return -1

    def put(self, key, value):
        if self.cap == 0:
            return
        elif key in self.mp:
            node = self.mp[key]
            node.val = value
            self.updateList(node)
        else:
            if self.currSize == self.cap:
                list_to_remove = self.freqList[self.minFreq]
                del self.mp[list_to_remove.tail.prev.key]
                list_to_remove.deleteNode(list_to_remove.tail.prev)
                self.currSize -= 1

            self.currSize += 1
            self.minFreq = 1

            new_list = List()
            if self.minFreq in self.freqList:
                new_list = self.freqList[self.minFreq]

            new_node = Node(key, value)
            new_list.addNewNode(new_node)
            self.freqList[self.minFreq] = new_list
            self.mp[key] = new_node