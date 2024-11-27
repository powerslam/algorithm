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

inf = 9876543210
n, m = map(int, input().split())

adj = [[] for _ in range(n + m + 2)]

s, e = 0, n + m + 1
for i in range(1, n + 1):
    _, *dsts = map(int, input().split())
    
    foward = edge(i, 1)
    backward = edge(s, 0)

    foward.dual = backward
    backward.dual = foward

    adj[s].append(foward)
    adj[i].append(backward)
    
    for dst in dsts:
        foward = edge(dst + n, 1)
        backward = edge(i, 0)

        foward.dual = backward
        backward.dual = foward

        adj[i].append(foward)
        adj[dst + n].append(backward)

for i in range(n + 1, n + m + 1):
    foward = edge(e, 1)
    backward = edge(i, 0)

    foward.dual = backward
    backward.dual = foward

    adj[i].append(foward)
    adj[e].append(backward)

total = 0
while True:
    prev = [-1] * (n + m + 2)
    path = [None] * (n + m + 2)

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
        assert path[i] is not None, f'{path} {i - n} {i}'
        flow = min(flow, path[i].residual())
        i = prev[i]

    i = e
    while i != s:
        path[i].add_flow(flow)
        i = prev[i]

    total += flow

print(total)    
