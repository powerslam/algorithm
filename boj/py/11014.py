import sys
input = lambda: sys.stdin.readline().strip()

from collections import deque

class edge:
    def __init__(self, dst, capacity):
        self.dst = dst
        self.capacity = capacity
        self.dual = None
        self.flow = 0

    def residual(self):
        return self.capacity - self.flow
    
    def add_flow(self, _flow):
        self.flow += _flow
        self.dual.flow -= _flow

    def __str__(self):
        return f'{self.dst} {self.capacity}'

def read():
    n, m = map(int, input().split())
    
    cnt = 0
    s, e = 0, n * m + 1
    adj = [[] for _ in range(n * m + 2)]
    board = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'x':
                cnt += 1
                continue

            if j % 2 == 1:
                forward = edge(e, 1)
                backward = edge(i * m + j + 1, 0)

                forward.dual = backward
                backward.dual = forward
                
                adj[i * m + j + 1].append(forward)
                adj[e].append(backward)

    dof = [[-1, -1], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 1]]
    for j in range(0, m, 2):
        for i in range(n):
            if board[i][j] == 'x':
                # cnt? += 1
                continue
        
            forward = edge(i * m + j + 1, 1)
            backward = edge(s, 0)

            forward.dual = backward
            backward.dual = forward
            
            adj[s].append(forward)
            adj[i * m + j + 1].append(backward)

            for dy, dx in dof:
                ny, nx = i + dy, j + dx
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue

                if board[ny][nx] == 'x':
                    continue

                forward = edge(ny * m + nx + 1, 1)
                backward = edge(i * m + j + 1, 0)

                forward.dual = backward
                backward.dual = forward

                adj[i * m + j + 1].append(forward)
                adj[ny * m + nx + 1].append(backward)

    return cnt, n, m, adj

def max_flow():
    total = 0
    while True:
        prev = [-1] * (n * m + 2)
        path = [None] * (n * m + 2)

        s, e = 0, n * m + 1
        q = deque([s])
        while q and prev[e] == -1:
            curr = q.popleft()

            for _edge in adj[curr]:
                nxt = _edge.dst
                if _edge.residual() > 0 and prev[nxt] == -1:
                    q.append(nxt)
                    prev[nxt] = curr
                    path[nxt] = _edge

                    if nxt == e:
                        break
        
        if prev[e] == -1:
            break

        i, flow = e, inf
        while i != s:
            flow = min(flow, path[i].residual())
            i = prev[i]

        i = e
        while i != s:
            path[i].add_flow(flow)
            i = prev[i]

        total += flow

    return total

inf = 9876543210
for _ in range(int(input())):
    x_cnt, n, m, adj = read()
    flow = max_flow()
    print(n * m - x_cnt - flow)
