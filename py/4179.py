import sys
input = lambda: sys.stdin.readline().strip()

class Node:
    def __init__(self):
        self.data = ''
        self.child = [0] * 30
        self.child_cnt = 0

    def __int__(self):
        return 1

    def __getitem__(self, key):
        return self.child[ord(key) - ord('a')]
    
    def __setitem__(self, key, value):
        self.child[ord(key) - ord('a')] = value
        self.child_cnt += 1

class Trie:
    def __init__(self):
        self.node = Node()

    def __getitem__(self, key):
        return self.node.child[ord(key) - ord('a')]

    def __setitem__(self, key, value):
        self.node.child[ord(key) - ord('a')] = value

    def add(self, word):
        head = self.node

        for w in word:
            if head[w] == 0:
                head[w] = Node()

            head = head[w]

        head.data = word

    def search(self, word):
        head = self.node

        for i in range(len(word)):
            if head.child_cnt == 0:
                return False

            if int(head[word[i]]) == 0:
                return False
                
            head = head[word[i]]
    
        return True

n, m = map(int, input().split())
prefix = Trie()
for _ in range(n):
    prefix.add(input())

ans = 0
for _ in range(m):
    if prefix.search(input()):
        ans += 1
print(ans)
