import sys
input = lambda: sys.stdin.readline().strip()

def init(node, nl, nr):
    if nl == nr:
        tree[node] = arr[nl]
        return tree[node]
    
    mid = nl + nr >> 1
    tree[node] = init(node * 2, nl, mid) ^ init(node * 2 + 1, mid + 1, nr)
    return tree[node]

def update_lazy(node, nl, nr):
    if lazy[node] != 0:
        if (nr - nl + 1) % 2 != 0:
            tree[node] ^= lazy[node]

        if nl != nr:
            lazy[node * 2] ^= lazy[node]
            lazy[node * 2 + 1] ^= lazy[node]
        
        lazy[node] = 0
        
def update_range(node, nl, nr, sl, sr, k):
    update_lazy(node, nl, nr)

    if sr < nl or nr < sl:
        return
    
    if sl <= nl and nr <= sr:
        lazy[node] ^= k
        update_lazy(node, nl, nr)
        return

    mid = nl + nr >> 1
    update_range(node * 2, nl, mid, sl, sr, k)
    update_range(node * 2 + 1, mid + 1, nr, sl, sr, k)
    tree[node] = tree[node * 2] ^ tree[node * 2 + 1]

def query(node, nl, nr, sl, sr):
    update_lazy(node, nl, nr)
    
    if sr < nl or nr < sl:
        return 0
    
    if sl <= nl and nr <= sr:
        return tree[node]
    
    mid = nl + nr >> 1
    return query(node * 2, nl, mid, sl, sr) ^ query(node * 2 + 1, mid + 1, nr, sl, sr)

n = int(input())
arr = list(map(int, input().split()))
tree = [0] * 4 * n
lazy = [0] * 4 * n
init(1, 0, n - 1)

for _ in range(int(input())):
    o, *param = map(int, input().split())
    if o == 1:
        i, j, k = param
        update_range(1, 0, n - 1, i, j, k)

    else:
        i, j = param
        print(query(1, 0, n - 1, i, j))
