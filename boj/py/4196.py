import sys
sys.setrecursionlimit(int(1e6))
input = lambda: sys.stdin.readline().strip()

def dfs(x):
    global id
    id += 1
    root[x] = id
    st.append(x)

    res = root[x]
    for nxt in adj[x]:
        if root[nxt] == 0:
            res = min(res, dfs(nxt))
        elif not visited[nxt]:
            res = min(res, root[nxt])

    if res == root[x]:
        scc = []
        while True:
            t = st.pop()
            visited[t] = True
            scc_id[t] = len(ans)
            scc.append(t)
            if t == x: break
        ans.append(scc)
    return res

t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        adj[a].append(b)

    id = 0
    root = [0] * (v + 1)
    visited = [False] * (v + 1)
    st, ans = [], []
    scc_id = [0] * (v + 1)

    for i in range(1, v + 1):
        if root[i] == 0:
            dfs(i)

    indeg = [0] * len(ans)
    for u in range(1, v + 1):
        for w in adj[u]:
            if scc_id[u] != scc_id[w]:
                indeg[scc_id[w]] += 1

    result = sum(1 for d in indeg if d == 0)
    print(result)
