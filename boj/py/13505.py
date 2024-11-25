import sys
input = lambda: sys.stdin.readline().strip()

class Node:
    def __init__(self):
        self.bit = [None, None]
        self.data = -1

class Trie:
    def __init__(self):
        self.head = Node()
    
    def add(self, value):
        head = self.head

        for bit in range(31, -1, -1):
            key = int((value & (1 << bit)) > 0)
            if head.bit[key] is None:
                head.bit[key] = Node()
            
            head = head.bit[key]

        head.data = value

    def xor(self, value):
        head = self.head

        res = 0
        for bit in range(31, -1, -1):
            key = int((value & (1 << bit)) > 0)
            if head.bit[1 - key] is not None:
                head = head.bit[1 - key]
                res += (1 << bit)
                continue

            head = head.bit[key]
            
        return res

n = int(input())
trie = Trie()
nums = list(map(int, input().split()))
for num in nums:
    trie.add(num)

ans = 0
for num in nums:
    ans = max(ans, trie.xor(num))

print(ans)
