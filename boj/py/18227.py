import sys
sys.setrecursionlimit(int(1e6))
input = lambda: sys.stdin.readline().strip()

def dfs(v, d):
    if visited[v]:
        return
    
    visited[v] = True

    global node_num

    depth[v] = d

    node_num += 1
    tree_idx[v][0] = node_num

    for nxt in adj[v]:
        if visited[nxt]:
            continue
        
        dfs(nxt, d + 1)

    tree_idx[v][1] = node_num

def update(node, nl, nr, idx):
    if idx < nl or nr < idx:
        return
    
    tree[node] += 1
    if nl != nr:
        mid = nl + nr >> 1
        update(node * 2, nl, mid, idx)
        update(node * 2 + 1, mid + 1, nr, idx)

def query(node, nl, nr, sl, sr):
    if sr < nl or nr < sl:
        return 0
    
    if sl <= nl and nr <= sr:
        return tree[node]

    mid = nl + nr >> 1
    l = query(node * 2, nl, mid, sl, sr)
    r = query(node * 2 + 1, mid + 1, nr, sl, sr)
    
    return l + r

node_num = 0
n, c = map(int, input().split())
tree = [0] * 800_004
depth = [0] * 200_001
visited = [False] * 200_001
tree_idx = [[0, 0] for _ in range(200_001)]
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

dfs(c, 1)
# print(tree_idx)

q = int(input())
for _ in range(q):
    o, a = map(int, input().split())
    if o == 1:
        update(1, 1, n, tree_idx[a][0])

    else:
        print(query(1, 1, n, tree_idx[a][0], tree_idx[a][1]) * depth[a])
