import sys
sys.setrecursionlimit(int(1e6))
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)

id = 0
root, scc, st = [0] * (n + 1), [], []
visited = [False] * (n + 1)

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
        scc.append([])
        while True:
            t = st.pop()
            scc[-1].append(t)
            visited[t] = True
            if t == v: break

    return res

for i in range(1, n + 1):
    if root[i] == 0:
        dfs(i)

print('Yes' if len(scc) == 1 else 'No')