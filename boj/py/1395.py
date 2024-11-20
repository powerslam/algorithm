import sys
input = lambda: sys.stdin.readline().strip()

def update_lazy(node, nl, nr):
    if lazy[node] != 0:
        tree[node] = (nr - nl + 1) - tree[node]

        if nl != nr:
            lazy[node * 2] = 1 - lazy[node * 2]
            lazy[node * 2 + 1] = 1 - lazy[node * 2 + 1]
        
        lazy[node] = 0
        
def update_range(node, nl, nr, sl, sr):
    update_lazy(node, nl, nr)

    if sr < nl or nr < sl:
        return
    
    if sl <= nl and nr <= sr:
        lazy[node] = 1 - lazy[node]
        update_lazy(node, nl, nr)
        return

    mid = nl + nr >> 1
    update_range(node * 2, nl, mid, sl, sr)
    update_range(node * 2 + 1, mid + 1, nr, sl, sr)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(node, nl, nr, sl, sr):
    update_lazy(node, nl, nr)
    
    if sr < nl or nr < sl:
        return 0
    
    if sl <= nl and nr <= sr:
        return tree[node]
    
    mid = nl + nr >> 1
    return query(node * 2, nl, mid, sl, sr) + query(node * 2 + 1, mid + 1, nr, sl, sr)

n, m = map(int, input().split())
tree = [0] * 4 * n
lazy = [0] * 4 * n

for _ in range(m):
    o, s, t = map(int, input().split())
    if o == 0:
        update_range(1, 0, n - 1, s - 1, t - 1)

    else:
        print(query(1, 0, n - 1, s - 1, t - 1))
