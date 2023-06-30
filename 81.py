class Node:
    def __init__(self):
        self.child = [None, None]

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        curr = self.root
        for c in s:
            c = int(c)
            if curr.child[c] == None:
                curr.child[c] = Node()
            curr = curr.child[c]
        
    def getmax(self, s):
        curr = self.root
        res = 0
        for c in s:
            c = int(c)
            if curr.child[1 - c] != None:
                curr = curr.child[1 - c]
                res = 2 * res + 1
            elif curr.child[c] != None:
                curr = curr.child[c]
                res = 2 * res
        return res

def maxXorQueries(arr, queries):
	n = len(arr)
	arr.sort()
	trie = Trie()
	k = max([len("{:b}".format(el)) for el in arr])
	m = len(queries)
	for i in range(m):
		queries[i].append(i)
	queries.sort(key = lambda p: p[1])
	i = 0
	res = [-1] * m
	i = 0
	for x, mx, j in queries:
		while i < n and arr[i] <= mx:
			trie.insert("{:032b}".format(arr[i]))
			i += 1
		if i > 0:
			res[j] = trie.getmax("{:032b}".format(x))
	return res  