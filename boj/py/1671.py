import sys
sys.setrecursionlimit(int(1e6))
input = lambda: sys.stdin.readline().strip()

n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
info.sort()

adj = [[] for _ in range(n + 1)]
for i in range(1, n):
    for j in range(i):
        if info[j][0] <= info[i][0] and info[j][1] <= info[i][1] and info[j][2] <= info[i][2]:
            adj[i].append(j)

def dfs(v):
    for nxt in adj[v]:
        if visited[nxt]: continue
        visited[nxt] = True

        if assign[nxt] == -1 or dfs(assign[nxt]):
            assign[nxt] = v
            return 1
    
    return 0

ans = 0
assign = [-1] * n
for i in range(n):
    visited = [False] * n
    ans += dfs(i)

    visited = [False] * n
    ans += dfs(i)

# print(assign)
print(n - ans)
