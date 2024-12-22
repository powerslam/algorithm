import sys
input = lambda: sys.stdin.readline().strip()

from collections import deque

class Edge:
    def __init__(self, dst, capacity, cost):
        self.dst = dst
        self.capacity = capacity
        self.cost = cost
        self.dual = None
        self.flow = 0

    def residual(self):
        return self.capacity -  self.flow
    
    def add_flow(self, _flow):
        self.flow += _flow
        self.dual.flow -= _flow

maxN, maxV = 100, 202
s, e, INF = maxV - 1, maxV - 2, int(1e8)

n, m = map(int, input().split())
adj = [[] for _ in range(maxV)]

people = list(map(int, input().split()))
for i in range(maxN, maxN + n):
    forward = Edge(e, people[i - maxN], 0)
    backward = Edge(i, 0, 0)

    forward.dual = backward
    backward.dual = forward

    adj[i].append(forward)
    adj[e].append(backward)

bookstores = list(map(int, input().split()))
for i in range(m):
    forward = Edge(i, bookstores[i], 0)
    backward = Edge(s, 0, 0)

    forward.dual = backward
    backward.dual = forward

    adj[s].append(forward)
    adj[i].append(backward)

for i in range(m):
    restrict = list(map(int, input().split()))
    for j in range(maxN, maxN + n):
        forward = Edge(j, restrict[j - maxN], 0)
        backward = Edge(i, 0, 0)

        forward.dual = backward
        backward.dual = forward

        adj[i].append(forward)
        adj[j].append(backward)

for i in range(m):
    costs = list(map(int, input().split()))
    for j in range(maxN, maxN + n):
        adj[i][j - maxN + 1].cost = costs[j - maxN]
        adj[i][j - maxN + 1].dual.cost = -costs[j - maxN]

total_flow, total_cost = 0, 0
while True:
    prev = [-1] * maxV
    path = [None] * maxV
    inQ = [False] * maxV
    dist = [INF] * maxV

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
print(total_cost)
