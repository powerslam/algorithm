import sys
sys.setrecursionlimit(int(1e6))
input = lambda: sys.stdin.readline().strip()

id = 0
v, e = map(int, input().split())
adj = [[] for _ in range(v + 1)]
root = [0] * (v + 1)
visited = [False] * (v + 1)
ans, st = [], []

for _ in range(e):
    a, b = map(int, input().split())
    adj[a].append(b)

def dfs(v):
    global id
    id += 1
    root[v] = id
    st.append(v)

    res = root[v]
    for nxt in adj[v]:
        if root[nxt] == 0: res = min(res, dfs(nxt))
        elif not visited[nxt]: res = min(res, root[nxt])
    
    if res == root[v]:
        ans.append([])
        while True:
            t = st.pop()
            ans[-1].append(t)
            visited[t] = True
            if t == v: break

    return res

for i in range(1, v + 1):
    if root[i] == 0:
        dfs(i)

print(len(ans))
ans = sorted([sorted(scc) for scc in ans])
for scc in ans:
    scc += [-1]
    print(*scc)
