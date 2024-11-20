import sys
input = lambda: sys.stdin.readline().strip()

class Node:
    def __init__(self):
        self.child = [0, 0]
        self.cnt = 0
        self.data = 0
    
    def __int__(self):
        return 1

class Trie:
    def __init__(self):
        self.head = Node()
    
    def insert(self, data):
        head = self.head
        while data != 0:
            if int(head.child[data & 1]) == 0:
                head.child[data & 1] = Node()

            head = head.child[data & 1]
            data >>= 1
        
        head.data = data
        head.cnt += 1

    def remove(self, data):
        head = self.head
        while data != 0:
            head = head.child[data & 1]
            data >>= 1
        
        head.cnt -= 1
        if head.cnt == 0:
            head.data = 0

    def xor(self, data):
        head = self.head
        ret, pos = 0, 0
        while head.data == 0:
            idx = data & 1
            if int(head.child[1 - idx]) == 0:
                return ret

            head = head.child[1 - idx]
            ret = (ret << pos) + (1 - idx)
            data >>= 1

        return ret

trie = Trie()
m = int(input())
for _ in range(m):
    o, x = map(int, input().split())
    if o == 1: trie.insert(x)
    elif o == 2: trie.remove(x)
    else: print(trie.xor(x))
