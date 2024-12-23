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

def solve(v, e_cnt):
    maxV, INF = v + 1, int(1e8)
    adj = [[] for _ in range(maxV * 2)]

    for i in range(1, maxV):
        forward = Edge(i + maxV, 1 , 0) # in
        backward = Edge(i, 0, 0)       # out
        
        forward.dual = backward
        backward.dual = forward
        
        adj[i].append(forward)
        adj[i + maxV].append(backward)

    for _ in range(e_cnt):
        a, b, c = map(int, input().split())
        forward = Edge(b, 1, c)
        backward = Edge(a + maxV, 0, -c)

        forward.dual = backward
        backward.dual = forward

        adj[a + maxV].append(forward)
        adj[b].append(backward)

    s, e = 1 + maxV, v
    total_cost = 0

    for _ in range(2):
        prev = [-1] * maxV * 2
        path = [None] * maxV * 2
        inQ = [False] * maxV * 2
        dist = [INF] * maxV * 2

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

    return total_cost

while True:
    try:
        v, e = map(int, input().split())
        print(solve(v, e))

    except:
        break
