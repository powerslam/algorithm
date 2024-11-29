import sys
sys.setrecursionlimit(int(1e6))
input = lambda: sys.stdin.readline().strip()

n, m, k = map(int, input().split())
adj = [[] for _ in range(2 * n + 1)]
for i in range(0, n * 2, 2):
    cnt, *param = map(int, input().split())
    for p in param:
        adj[i + 1].append(p)
        adj[i + 2].append(p)

def dfs(v):
    for nxt in adj[v]:
        if visited[nxt]: continue
        visited[nxt] = True

        if assign[nxt] == -1 or dfs(assign[nxt]):
            assign[nxt] = v
            return 1

    return 0

ans1 = 0
assign = [-1] * (m + 1)
for i in range(1, 2 * n + 1, 2):
    visited = [False] * (m + 1)
    ans1 += dfs(i)

ans2 = 0
for i in range(2, 2 * n + 1, 2):
    visited = [False] * (m + 1)
    ans2 += dfs(i)

    if ans2 == k:
        break

print(ans1 + ans2)
