import sys
input = lambda: sys.stdin.readline().strip()

sys.setrecursionlimit(int(1e6))

from bisect import bisect_right as upper_bound

node_num = 0
def dfs(v):
    global node_num

    node_num += 1
    colors[node_num] = arr[v]
    tree_node[v][0] = node_num

    for nxt in adj[v]:
        if tree_node[nxt][0] == 0:
            dfs(nxt)

    tree_node[v][1] = node_num

n, m, c = map(int, input().split())
colors = [0] * (n + 1)
arr = [0] + list(map(int, input().split()))
tree_node = [[0, 0] for _ in range(n + 1)]
adj = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

dfs(1)

tree = [[] for _ in range(4 * n + 200)]
mod = int(1e9) + 7

def init_tree(node, nl, nr):
    if nl == nr:
        tree[node].append(colors[nl])
        return
    
    mid = nl + nr >> 1
    init_tree(node * 2, nl, mid)
    init_tree(node * 2 + 1, mid + 1, nr)

    l, r = nl, mid + 1
    while l <= mid and r <= nr:
        if tree[node * 2][l - nl] < tree[node * 2 + 1][r - mid - 1]:
            tree[node].append(tree[node * 2][l - nl])
            l += 1

        else:
            tree[node].append(tree[node * 2 + 1][r - mid - 1])
            r += 1

    while l <= mid:
        tree[node].append(tree[node * 2][l - nl])
        l += 1

    while r <= nr:
        tree[node].append(tree[node * 2 + 1][r - mid - 1])
        r += 1

def query(node, nl, nr, sl, sr, key):
    if sr < nl or nr < sl:
        return 0
    
    if sl <= nl and nr <= sr:
        ret = upper_bound(tree[node], key)
        return ret
    
    mid = nl + nr >> 1
    return query(node * 2, nl, mid, sl, sr, key) + query(node * 2 + 1, mid + 1, nr, sl, sr, key)

init_tree(1, 1, n)

ans = 0
for _ in range(m):
    v, c = map(int, input().split())
    ans += query(1, 1, n, tree_node[v][0], tree_node[v][1], c)

print(ans % mod)
