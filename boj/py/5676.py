import sys
input = lambda: sys.stdin.readline().strip()

def init(node, nl, nr):
    if nl == nr:
        tree[node] = arr[nl]
        return tree[node]
    
    mid = nl + nr >> 1
    tree[node] = init(node * 2, nl, mid) * init(node * 2 + 1, mid + 1, nr)
    return tree[node]

def update(node, nl, nr, k, v):
    if k < nl or nr < k:
        return tree[node]
    
    if nl == nr:
        tree[node] = v
        return tree[node]

    mid = nl + nr >> 1
    left = update(node * 2, nl, mid, k, v)
    right = update(node * 2 + 1, mid + 1, nr, k, v)
    tree[node] = left * right
    return tree[node]

def query(node, nl, nr, sl, sr):
    if sr < nl or nr < sl:
        return 1
    
    if sl <= nl and nr <= sr:
        return tree[node]
    
    mid = nl + nr >> 1
    return query(node * 2, nl, mid, sl, sr) * query(node * 2, mid + 1, nr, sl, sr)

def convert(val):
    return -1 if val < 0 else 1 if val > 0 else 0

while True:
    try:
        n, k = map(int, input().split())
        arr = [convert(i) for i in map(int, input().split())]
        tree = [0] * 4 * n
        init(1, 0, n - 1)
    
        ans = ''
        for _ in range(k):
            o, *param = input().split()
            if o == 'C':
                i, v = map(int, param)
                update(1, 0, n - 1, i - 1, convert(v))

            else:
                i, j = map(int, param)
                ret = query(1, 0, n - 1, i - 1, j - 1)
                ans += ['0', '+', '-'][ret]
    
        print(ans)
    
    except:
        # print(e)
        break
