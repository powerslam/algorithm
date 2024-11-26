import sys
input = lambda: sys.stdin.readline().strip()

lim = 9876543210
n = int(input())
arr = list(map(int, input().split()))
q = int(input())

tree = [[lim, -lim, 0] for _ in range(4 * n)]
def init(node, nl, nr):
    if nl == nr:
        tree[node][0] = arr[nl]
        tree[node][1] = arr[nl]
        return

    mid = nl + nr >> 1
    init(node * 2, nl, mid)
    init(node * 2 + 1, mid + 1, nr)

    tree[node][0] = min(tree[node * 2][0], tree[node * 2 + 1][0])
    tree[node][1] = max(tree[node * 2][1], tree[node * 2 + 1][1])
    tree[node][2] = max(tree[node * 2][2], tree[node * 2 + 1][2], tree[node * 2 + 1][1] - tree[node * 2][0])

def update(node, nl, nr, idx, v):
    if idx < nl or nr < idx:
        return
    
    if nl == nr:
        tree[node][2] = 0
        tree[node][0] = tree[node][1] = v
        return

    mid = nl + nr >> 1
    update(node * 2, nl, mid, idx, v)
    update(node * 2 + 1, mid + 1, nr, idx, v)

    tree[node][0] = min(tree[node * 2][0], tree[node * 2 + 1][0])
    tree[node][1] = max(tree[node * 2][1], tree[node * 2 + 1][1])
    tree[node][2] = max(tree[node * 2][2], tree[node * 2 + 1][2], tree[node * 2 + 1][1] - tree[node * 2][0])

def query(node, nl, nr, sl, sr):
    if sr < nl or nr < sl:
        return [lim, -lim, 0]
    
    if sl <= nl and nr <= sr:
        return tree[node]

    mid = nl + nr >> 1
    left = query(node * 2, nl, mid, sl, sr)
    right = query(node * 2 + 1, mid + 1, nr, sl, sr)

    ret1 = min(left[0], right[0])
    ret2 = max(left[1], right[1])
    ret3 = max(left[2], right[2], right[1] - left[0])
    return [ret1, ret2, ret3]

init(1, 0, n - 1)
# print(tree)

for _ in range(q):
    o, a, b = map(int, input().split())
    if o == 1:
        update(1, 0, n - 1, a - 1, b)

    else:
        a -= 1
        b -= 1
        print(query(1, 0, n - 1, a, b)[2])    
