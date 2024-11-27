import sys
input = lambda: sys.stdin.readline().strip()

from collections import deque

max_v = 52
inf = 9876543210

n = int(input())
c = [[0] * max_v for _ in range(max_v)]
f = [[0] * max_v for _ in range(max_v)]
adj = [[] for _ in range(max_v)]

ctol = lambda c: (ord(c) - ord('A')) if c <= 'Z' else (ord(c) - ord('a') + 26)

for _ in range(n):
    u, v, w = input().split()
    u, v = ctol(u), ctol(v)
    w = int(w)

    c[u][v] += w
    c[v][u] += w

    adj[u].append(v)
    adj[v].append(u)

total, s, e = 0, ctol('A'), ctol('Z')
while True:
    prev = [-1] * max_v
    q = deque([])
    q.append(s)

    # 증가 경로를 하나 찾음
    while q and prev[e] == -1:
        curr = q.popleft()
        for nxt in adj[curr]:
            if c[curr][nxt] - f[curr][nxt] > 0 and prev[nxt] == -1:
                q.append(nxt)
                prev[nxt] = curr
                if nxt == e:
                    break

    # 증가 경로가 없으면 탈출
    if prev[e] == -1:
        break

    # 차단 간선 찾기
    i, flow = e, inf
    while i != s:
        flow = min(flow, c[prev[i]][i] - f[prev[i]][i])
        i = prev[i]

    # 모든 간선에 차단 간선에 남은 용량만큼 더하기
    i = e
    while i != s:
        f[prev[i]][i] += flow
        f[i][prev[i]] -= flow
        i = prev[i]
    
    total += flow

print(total)
