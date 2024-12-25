import sys
input = lambda: sys.stdin.readline().strip()

from collections import deque

class Edge:
    def __init__(self, dst, capacity, cost):
        self.dst = dst
        self.capacity = capacity
        self.dual = None
        self.flow = 0
        self.cost = cost

    def residual(self):
        return self.capacity -  self.flow
    
    def add_flow(self, _flow):
        self.flow += _flow
        self.dual.flow -= _flow

n, p = map(int, input().split())
adj = [[] for _ in range(n + 2)]

for _ in range(p):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
    
    forward = Edge(v, 1, c)
    backward = Edge(u, 0, -c)

    forward.dual = backward
    backward.dual = forward

    adj[u].append(forward)
    adj[v].append(backward)

    forward = Edge(u, 1, c)
    backward = Edge(v, 0, -c)

    forward.dual = backward
    backward.dual = forward

    adj[v].append(forward)
    adj[u].append(backward)

def solve(s, e):
    ret, INF = 0, 9876543210
    for _ in range(2):
        prev = [-1] * (n + 2)
        path = [None] * (n + 2)
        inQ = [False] * (n + 2)
        dist = [INF] * (n + 2)

        dist[s] = 0
        inQ[s] = True
        q = deque([s])

        while q:
            curr = q.popleft()
            inQ[curr] = False

            for edge in adj[curr]:
                nxt = edge.dst

                if edge.residual() > 0 and dist[nxt] > dist[curr] + edge.cost:
                    prev[nxt] = curr
                    path[nxt] = edge
                    dist[nxt] = dist[curr] + edge.cost

                    if not inQ[nxt]:
                        inQ[nxt] = True
                        q.append(nxt)

        if prev[e] == -1:
            break

        i, flow = e, INF
        while i != s:
            flow = min(flow, path[i].residual())
            i = prev[i]

        i = e
        while i != s:
            ret += flow * path[i].cost
            path[i].add_flow(flow)
            i = prev[i]
    
    return ret

print(solve(0, n - 1))
