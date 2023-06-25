hm = {}
k = 'a'
v = 0
hm[k] = v
while v < 26:
    k = chr(ord(k)+1)
    v += 1
    hm[k] = v

def getIndex(c):
    return hm[c]

class Trie:
    def __init__(self):
        self.char = ['']*26
        self.ptr = [None]*26
        self.flag = False
    
    def insert(self, word):
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
                    
            elif self.char[i] == w:
                curr = self.ptr[i]
            else:
                self.char[i] = w
                self.ptr[i] = Trie()
                curr = self.ptr[i]
        curr.flag = True
        return
    
    def findWord(self, word):
        curr = None
        for w in word:
            i = getIndex(w)
            if curr is not None:
                if curr.char[i] == w:
                    curr = curr.ptr[i]
                else:
                    return False
            elif self.char[i] == w:
                curr = self.ptr[i]
            else:
                return False
        
        return curr.flag

    def findCompleteWord(self, word):
        curr = None
        for w in word:
            i = getIndex(w)
            if curr is not None:
                if curr.char[i] == w:
                    curr = curr.ptr[i]
                    if not curr.flag:
                        return False
                else:
                    return False
            elif self.char[i] == w:
                curr = self.ptr[i]
                if not curr.flag:
                    return False
            else:
                return False
            
        return True
    
root = Trie()
root.insert('abcd')
root.insert('a')
root.insert('ab')
root.insert('abc')
print(root.findWord('abcd'))   
print(root.findCompleteWord('abc'))
                
                
                
    
        