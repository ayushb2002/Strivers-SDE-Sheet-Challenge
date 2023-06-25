def getIndex(c):
    hm = {}
    k = 'a'
    v = 0
    hm[k] = v
    while v < 26:
        k = chr(ord(k)+1)
        v += 1
        hm[k] = v
    return hm[c]

class Trie:
    def __init__(self):
        self.char = ['']*26
        self.ptr = [None]*26
        self.flag = False
    
    def insert(self, word):
        res = 0
        curr = None
        for w in word:
            i = getIndex(w)
            if curr is not None:
                if curr.char[i] == w:
                    curr = curr.ptr[i]
                else:
                    curr.char[i] = w
                    curr.ptr[i] = Trie()
                    curr = curr.ptr[i]
                    res += 1
                    
            elif self.char[i] == w:
                curr = self.ptr[i]
            else:
                self.char[i] = w
                self.ptr[i] = Trie()
                curr = self.ptr[i]
                res += 1
        curr.flag = True
        return res
    
def distinctSubstring(word):
    res = 0
    root = Trie()
    n = len(word)
    for i in range(n):
        res += root.insert(word[i:])
    
    return res + 1

print(distinctSubstring("abab"))