import sys
sys.setrecursionlimit(int(1e6))
input = lambda: sys.stdin.readline().strip()

def dfs(v):
    global node_num

    node_num += 1
    tree_node[v][0] = node_num
    for nxt in adj[v]:
        dfs(nxt)

    tree_node[v][1] = node_num

n = int(input())
arr = list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]
for i in range(1, n):
    adj[arr[i]].append(i + 1)

node_num = 0
tree_node = [[0, 0] for _ in range(n + 1)]

dfs(1)

tree = [0] * 4 * (n + 1)
lazy = [0] * 4 * (n + 1)

def init(node, nl, nr):
    if nl == nr:
        tree[node] = 1
        return 1
    
    mid = nl + nr >> 1
    tree[node] = init(node * 2, nl, mid) + init(node * 2 + 1, mid + 1, nr)
    return tree[node]

init(1, 1, n)

def update_lazy(node, nl, nr):
    if lazy[node] != 0:
        # 이미 켜져 있거나 꺼져있는 상황에 대비해야 함
        tree[node] = (nr - nl + 1) if lazy[node] > 0 else 0
        
        if nl != nr:
            lazy[node * 2] = lazy[node]
            lazy[node * 2 + 1] = lazy[node]

        lazy[node] = 0

def update_range(node, nl, nr, sl, sr, diff):
    update_lazy(node, nl, nr)
    if sr < nl or nr < sl:
        return
    
    if sl <= nl and nr <= sr:
        lazy[node] = diff
        update_lazy(node, nl, nr)
        return

    mid = nl + nr >> 1
    update_range(node * 2, nl, mid, sl, sr, diff)
    update_range(node * 2 + 1, mid + 1, nr, sl, sr, diff)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(node, nl, nr, sl, sr):
    update_lazy(node, nl, nr)
    if sr < nl or nr < sl:
        return 0
    
    if sl <= nl and nr <= sr:
        return tree[node]
    
    mid = nl + nr >> 1
    left = query(node * 2, nl, mid, sl, sr)
    right = query(node * 2 + 1, mid + 1, nr, sl, sr)
    return left + right

m = int(input())
for _ in range(m):
    o, i = map(int, input().split())
    if o == 1:
        update_range(1, 1, n, tree_node[i][0] + 1, tree_node[i][1], 1)
    
    elif o == 2:
        update_range(1, 1, n, tree_node[i][0] + 1, tree_node[i][1], -1)

    else:
        print(query(1, 1, n, tree_node[i][0] + 1, tree_node[i][1]))
