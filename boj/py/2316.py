import sys
input = lambda: sys.stdin.readline().strip()

from collections import deque

class Edge:
    def __init__(self, dst, capacity):
        self.dst = dst
        self.capacity = capacity
        self.dual = None
        self.flow = 0

    def residual(self):
        return self.capacity -  self.flow
    
    def add_flow(self, _flow):
        self.flow += _flow
        self.dual.flow -= _flow

n, p = map(int, input().split())
adj = [[] for _ in range(n * 2 + 1)]

for i in range(n):
    u = i * 2
    v = u + 1

    forward = Edge(v, 1)
    backward = Edge(u, 0)

    forward.dual = backward
    backward.dual = forward

    adj[u].append(forward)
    adj[v].append(backward)

for _ in range(p):
    u, v = map(int, input().split())
    forward = Edge(v * 2 - 2, 1)
    backward = Edge(u * 2 - 1, 0)

    forward.dual = backward
    backward.dual = forward

    adj[u * 2 - 1].append(forward)
    adj[v * 2 - 2].append(backward)

    forward = Edge(v * 2 - 1, 0)
    backward = Edge(u * 2 - 2, 1)

    forward.dual = backward
    backward.dual = forward

    adj[u * 2 - 2].append(forward)
    adj[v * 2 - 1].append(backward)

inf = 9876543210
total, s, e = 0, 1, 2
while True:
    prev = [-1] * (n * 2 + 1)
    path = [None] * (n * 2 + 1)

    q = deque([s])
    while q and prev[e] == -1:
        curr = q.popleft()
        for edge in adj[curr]:
            nxt = edge.dst
            if edge.residual() > 0 and prev[nxt] == -1:
                prev[nxt] = curr
                path[nxt] = edge
                q.append(nxt)

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

print(total)
