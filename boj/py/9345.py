import sys
input = lambda: sys.stdin.readline().strip()

inf = int(1e9)

def init(node, nl, nr):
    if nl == nr:
        tree[node][0] = pos[nl]
        tree[node][1] = pos[nr]
        return tree[node]

    mid = nl + nr >> 1
    left = init(node * 2, nl, mid)
    right = init(node * 2 + 1, mid + 1, nr)

    tree[node][0] = min(left[0], right[0])
    tree[node][1] = max(left[1], right[1])
    return tree[node]

def update(node, nl, nr, k, v):
    if k < nl or nr < k:
        pass

    elif nl == nr:
        tree[node][0] = v
        tree[node][1] = v
    
    else:
        mid = nl + nr >> 1
        left = update(node * 2, nl, mid, k, v)
        right = update(node * 2 + 1, mid + 1, nr, k, v)

        tree[node][0] = min(left[0], right[0])
        tree[node][1] = max(left[1], right[1])
        
    return tree[node]

def query(node, nl, nr, sl, sr):
    if sr < nl or nr < sl:
        return [inf, 0]

    if sl <= nl and nr <= sr:
        return tree[node]

    mid = nl + nr >> 1
    left = query(node * 2, nl, mid, sl, sr)
    right = query(node * 2 + 1, mid + 1, nr, sl, sr)

    return [min(left[0], right[0]), max(left[1], right[1])]

for _ in range(int(input())):
    n, k = map(int, input().split())
    
    tree = [[inf, 0] for _ in range(4 * n)]
    pos = list(range(n))

    init(1, 0, n - 1)

    for _ in range(k):
        q, a, b = map(int, input().split())

        if q == 0:
            pos[a], pos[b] = pos[b], pos[a]
            update(1, 0, n - 1, a, pos[a])
            update(1, 0, n - 1, b, pos[b])

        else:
            ret = query(1, 0, n - 1, a, b)
            print('YES' if ret[0] == a and ret[1] == b else 'NO')
