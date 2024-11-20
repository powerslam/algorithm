import sys
input = lambda: sys.stdin.readline().strip()

def init(node, nl, nr):
    if nl == nr:
        if nl < n:
            tree[node] = 1
            return 1

        return 0

    mid = nl + nr >> 1
    tree[node] = init(node * 2, nl, mid) + init(node * 2 + 1, mid + 1, nr)
    return tree[node]

def update(node, nl, nr, k1, k2):
    next__ = False
    if nl <= k1 <= nr:
        tree[node] -= 1
        next__ = True

    if nl <= k2 <= nr:
        tree[node] += 1
        next__ = True

    if next__ and nl != nr:
        mid = nl + nr >> 1
        update(node * 2, nl, mid, k1, k2)
        update(node * 2 + 1, mid + 1, nr, k1, k2)

def query(node, nl, nr, sl, sr):
    if nr < sl or sr < nl:
        return 0
    
    if sl <= nl and nr <= sr:
        return tree[node]

    mid = nl + nr >> 1
    return query(node * 2, nl, mid, sl, sr) + query(node * 2 + 1, mid + 1, nr, sl, sr)

for _ in range(int(input())):
    n, m = map(int, input().split())
    top, arr = n, {i: n - i for i in range(1, n + 1)}
    tree = [0] * 4 * (n + m)
    init(1, 0, n + m)

    ans = ''
    for num in map(int, input().split()):
        if arr[num] == top - 1:
            ans += '0 '
        
        else:
            # print('arr[num] :', arr[num])
            ans += str(query(1, 0, n + m - 1, arr[num] + 1, top)) + ' '
            update(1, 0, n + m - 1, arr[num], top)
            arr[num] = top
            top += 1

    print(ans)
