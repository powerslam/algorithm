import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
cnt = [0] * (n + 1)
arr = []
for num in map(int, input().split()):
    cnt[num] += 1
    arr.append(cnt[num])

tree = [[] for _ in range(4 * n)]

def init(node, nl, nr):
    if nl == nr:
        tree[node].append(arr[nl])
        return
    
    mid = nl + nr >> 1
    init(node * 2, nl, mid)
    init(node * 2 + 1, mid + 1, nr)

    l, r = nl, mid + 1
    left = tree[node * 2]
    right = tree[node * 2 + 1]

    while l < mid + 1 and r <= nr:
        if left[l - nl] <= right[r - mid - 1]:
            tree[node].append(left[l - nl])
            l += 1

        else:
            tree[node].append(right[r - mid - 1])
            r += 1

    while l < mid + 1:
        tree[node].append(left[l - nl])
        l += 1

    while r <= nr:
        tree[node].append(right[r - mid - 1])
        r += 1

def query(node, nl, nr, sl, sr):
    if nl > sr or sl > nr: return 0

    if sl <= nl and nr <= sr:
        return tree[node][-1]
    
    mid = nl + nr >> 1
    x = query(node * 2, nl, mid, sl, sr)
    y = query(node * 2 + 1, mid + 1, nr, sl, sr)

    return max(x, y)

init(1, 0, n - 1)
m = int(input())
for _ in range(m):
    i, j = map(int, input().split())
    print(query(1, 0, n - 1, i - 1, j - 1))
