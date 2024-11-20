import sys
from collections import deque
input = lambda: sys.stdin.readline()

n = int(input())
board = [input().split() for _ in range(n)]

class pos:
    def __init__(self, x, y, res):
        self.x = x
        self.y = y
        self.res = res
        self.oper = ''

    def get(self) -> str:
        return self.get(self.x, self.y)

    def get(self, x, y) -> str:
        global board
        return board[y][x]

    def right(self) -> str:
        if self.x + 1 >= n: return 'x'
        return self.get(self.x + 1, self.y)
    
    def down(self) -> str:
        if self.y + 1 >= n: return 'x'
        return self.get(self.x, self.y + 1)

q = deque([pos(0, 0, int(board[0][0]))])
m, M = 987654321, -987654321
while len(q) != 0:
    now = q.popleft()

    r = now.right()
    if r != 'x':
        right = pos(now.x + 1, now.y, now.res)
        if now.oper != '':
            if now.oper == '+':
                right.res += int(r)
            
            elif now.oper == '-':
                right.res -= int(r)

            elif now.oper == '*':
                right.res *= int(r)

            q.append(right)

        else: 
            right.oper = r
            q.append(right)

    d = now.down()
    if d != 'x':
        down = pos(now.x, now.y + 1, now.res)
        if now.oper != '':
            if now.oper == '+':
                down.res += int(d)
            
            elif now.oper == '-':
                down.res -= int(d)

            elif now.oper == '*':
                down.res *= int(d)

            q.append(down)

        else: 
            down.oper = d
            q.append(down)

    if r == 'x' and d == 'x':
        m = min(m, now.res)
        M = max(M, now.res)

print(M, m)
