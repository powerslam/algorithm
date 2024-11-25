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
adj = [[] for _ in range(n + 1)]
arr = list(map(int, input().split()))
for i in range(1, n):
    adj[arr[i]].append(i + 1)

dfs(1)
# print(tree_node)

tree = [0] * n * 4
def update(node, nl, nr, idx, diff):
    if idx < nl or nr < idx:
        return
    
    tree[node] += diff
    if nl != nr:
        mid = nl + nr >> 1
        update(node * 2, nl, mid, idx, diff)
        update(node * 2 + 1, mid + 1, nr, idx, diff)

def query(node, nl, nr, sl, sr):
    if sr < nl or nr < sl:
        return 0
    
    if sl <= nl and nr <= sr:
        return tree[node]
    
    mid = nl + nr >> 1
    left = query(node * 2, nl, mid, sl, sr)
    right = query(node * 2 + 1, mid + 1, nr, sl, sr)
    return left + right

for _ in range(m):
    o, *param = map(int, input().split())
    if o == 1:
        i, w = param
        update(1, 1, n, tree_node[i][0], w)

    else:
        i = param[0]
        # print(tree)
        print(query(1, 1, n, tree_node[i][0], tree_node[i][1]))
