import sys
sys.setrecursionlimit(int(1e6))
input = lambda: sys.stdin.readline().strip()

node_num = 0
def dfs(v):
    global node_num

    node_num += 1
    tree_node[v][0] = node_num

    for nxt in adj[v]:
        dfs(nxt)

    tree_node[v][1] = node_num

n, m = map(int, input().split())
tree_node = [[0, 0] for _ in range(n + 1)]
roots = list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]

for i in range(1, n):
    adj[roots[i]].append(i + 1)

dfs(1)

tree = [0] * 4 * n
lazy = [0] * 4 * n

def update_lazy(node, nl, nr):
    if lazy[node] != 0:
        tree[node] += (nr - nl + 1) * lazy[node]
        if nl != nr:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0

def update_range(node, nl, nr, sl, sr, diff):
    update_lazy(node, nl, nr)

    if sr < nl or nr < sl:
        return
    
    if sl <= nl and nr <= sr:
        lazy[node] += diff
        update_lazy(node, nl, nr)
        return
    
    mid = nl + nr >> 1
    update_range(node * 2, nl, mid, sl, sr, diff)
    update_range(node * 2 + 1, mid + 1, nr, sl, sr, diff)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(node, nl, nr, idx):
    update_lazy(node, nl, nr)
    if idx < nl or nr < idx:
        return 0
    
    if nl == nr:
        return tree[node]
    
    mid = nl + nr >> 1
    left = query(node * 2, nl, mid, idx)
    right = query(node * 2 + 1, mid + 1, nr, idx)
    return left + right

for _ in range(m):
    o, *param = map(int, input().split())
    if o == 1:
        i, w = param
        update_range(1, 1, n, tree_node[i][0], tree_node[i][1], w)
        
    else:
        i = param[0]
        print(query(1, 1, n, tree_node[i][0]))
        