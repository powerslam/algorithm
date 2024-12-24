import sys
input = lambda: sys.stdin.readline().strip()

from collections import deque

class Edge:
    def __init__(self, dst, capacity, cost):
        self.dst = dst
        self.capacity = capacity
        self.flow = 0
        self.cost = cost
        self.dual = None

    def add_flow(self, flow):
        self.flow += flow
        self.dual.flow -= flow

    def residual(self):
        return self.capacity - self.flow

n, m = map(int, input().split())
adj = [[] for _ in range(n + m + 2)]

s, e = n + m, n + m + 1
for i in range(n):
    forward = Edge(i, 1, 0)
    backward = Edge(s, 0, 0)
    
    forward.dual = backward
    backward.dual = forward
    
    adj[s].append(forward)
    adj[i].append(backward)

for i in range(n, n + m):
    forward = Edge(e, 1, 0)
    backward = Edge(i, 0, 0)
    
    forward.dual = backward
    backward.dual = forward
    
    adj[i].append(forward)
    adj[e].append(backward)

for i in range(n):
    cnt, *param = map(int, input().split())

    for j in range(0, cnt * 2, 2):
        forward = Edge(n + param[j] - 1, 1, -param[j + 1])
        backward = Edge(i, 0, param[j + 1])
        
        forward.dual = backward
        backward.dual = forward
        
        adj[i].append(forward)
        adj[n + param[j] - 1].append(backward)

total_flow, total_cost, INF = 0, 0, int(1e8)
while True:
    prev = [-1] * (n + m + 2)
    path = [None] * (n + m + 2)
    dist = [INF] * (n + m + 2)
    inQ = [False] * (n + m + 2)

    dist[s] = 0
    inQ[s] = True
    q = deque([s])

    while q:
        curr = q.popleft()
        inQ[curr] = False

        for edge in adj[curr]:
            nxt = edge.dst

            if edge.residual() > 0 and dist[nxt] > dist[curr] + edge.cost:
                dist[nxt] = dist[curr] + edge.cost
                prev[nxt] = curr
                path[nxt] = edge

                if not inQ[nxt]:
                    q.append(nxt)
                    inQ[nxt] = True

    if prev[e] == -1:
        break

    i, flow = e, INF
    while i != s:
        flow = min(flow, path[i].residual())
        i = prev[i]

    i = e
    while i != s:
        total_cost += flow * path[i].cost
        path[i].add_flow(flow)
        i = prev[i]

    total_flow += flow

print(total_flow)
print(-total_cost)
