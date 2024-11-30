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
adj = [[] for _ in range(n + 1)]
tree_node = [[0, 0] for _ in range(n + 1)]

arr = list(map(int, input().split()))
for i in range(1, n):
    adj[arr[i]].append(i + 1)

dfs(1)

tree1 = [0] * 4 * n
tree2 = [0] * 4 * n
lazy = [0] * 4 * n

def update_lazy(node, nl, nr):
	if lazy[node] != 0:
		tree1[node] += (nr - nl + 1) * lazy[node]
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
	tree1[node] = tree1[node * 2] + tree1[node * 2 + 1]

def query_lazy(node, nl, nr, sl, sr):
    update_lazy(node, nl, nr)
    if sr < nl or nr < sl:
        return 0
    
    if sl <= nl and nr <= sr:
        return tree1[node]
    
    mid = nl + nr >> 1
    left = query_lazy(node * 2, nl, mid, sl, sr)
    right = query_lazy(node * 2 + 1, mid + 1, nr, sl, sr)
    return left + right

def update(node, nl, nr, idx, diff):
    if idx < nl or nr < idx:
        return
    
    tree2[node] += diff
    if nl != nr:
        mid = nl + nr >> 1
        update(node * 2, nl, mid, idx, diff)
        update(node * 2 + 1, mid + 1, nr, idx, diff)
        tree2[node] = tree2[node * 2] + tree2[node * 2 + 1]

def query(node, nl, nr, sl, sr):
    if sr < nl or nr < sl:
        return 0
    
    if sl <= nl and nr <= sr:
        return tree2[node]
    
    mid = nl + nr >> 1
    left = query(node * 2, nl, mid, sl, sr)
    right = query(node * 2 + 1, mid + 1, nr, sl, sr)
    return left + right

direction = True
for _ in range(m):
    o, *param = map(int, input().split())
    if o == 1:
        i, w = param
        if direction:
            update_range(1, 1, n, tree_node[i][0], tree_node[i][1], w)

        else:
            update(1, 1, n, tree_node[i][0], w)
		
    elif o == 2:
        i = param[0]
        ret = query_lazy(1, 1, n, tree_node[i][0], tree_node[i][0])
        ret += query(1, 1, n, tree_node[i][0], tree_node[i][1]) 
        print(ret)

    else:
        direction = not direction
