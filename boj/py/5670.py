import sys
input = lambda: sys.stdin.readline().strip()

class Node:
    def __init__(self):
        self.data = ''
        self.child = [0] * 30
        self.child_cnt = 0

    def __int__(self):
        return 1

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
            if head.child[ord(w) - ord('a')] == 0:
                head.child[ord(w) - ord('a')] = Node()
                head.child_cnt += 1

            head = head.child[ord(w) - ord('a')]

        head.data = word

def dfs(v: Node, cnt: int):
    global ans

    if v.data != '':
        ans += cnt
        # print('ans : ', ans, cnt, v.data)
        if v.child_cnt > 0: cnt += 1
    
    elif v.child_cnt > 1:
        cnt += 1

    for i, c in enumerate(v.child):
        if c == 0:
            continue
        
        # print(chr(i + ord('a')), cnt)
        dfs(c, cnt)

def solve(words):
    global ans

    trie = Trie()
    
    prefix = set()
    for word in words:
        trie.add(word)
        prefix.add(word[0])

    for c in prefix:
        dfs(trie[c], 1)

    return ans / len(words)
    
while True:
    try:
        ans = 0
        n = int(input())
        words = [input() for _ in range(n)]
        print(f'{solve(words):.2f}')

    except EOFError:
        break

    except ValueError:
        break
