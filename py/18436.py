import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
tree1 = [0] * 4 * n
tree2 = [0] * 4 * n

even = [0] * n
odd = [0] * n
a = list(map(int, input().split()))
for i in range(len(a)):
    even[i] = int(a[i] % 2 == 0)
    odd[i] = 1 - even[i]

# print(even, odd)

def init(node, nl, nr):
    if nl == nr:
        # print(node, nl, odd[nl], even[nl])
        tree1[node] = odd[nl]
        tree2[node] = even[nl]
        return
    
    mid = nl + nr >> 1
    init(node * 2, nl, mid)
    init(node * 2 + 1, mid + 1, nr)

    tree1[node] = tree1[node * 2] + tree1[node * 2 + 1]
    tree2[node] = tree2[node * 2] + tree2[node * 2 + 1]

def query(node, nl, nr, sl, sr):
    if nl > sr or sl > nr:
        return 0, 0

    if sl <= nl and nr <= sr:
        return tree1[node], tree2[node]

    mid = nl + nr >> 1
    l1, l2 = query(node * 2, nl, mid, sl, sr)
    r1, r2 = query(node * 2 + 1, mid + 1, nr, sl, sr)

    return l1 + r1, l2 + r2

def update(node, nl, nr, idx, v):
    if nl > idx or idx > nr:
        return
    
    if nl == nr:
        tree1[node] = 1 - v
        tree2[node] = v
        return

    mid = nl + nr >> 1
    update(node * 2, nl, mid, idx, v)
    update(node * 2 + 1, mid + 1, nr, idx, v)

    tree1[node] = tree1[node * 2] + tree1[node * 2 + 1]
    tree2[node] = tree2[node * 2] + tree2[node * 2 + 1]

init(1, 0, n - 1)

m = int(input())
for _ in range(m):
    o, a, b = map(int, input().split())
    if o == 1:
        update(1, 0, n - 1, a - 1, int(b % 2 == 0))

    else:
        _o, _e = query(1, 0, n - 1, a - 1, b - 1)
        print(_e if o == 2 else _o)

