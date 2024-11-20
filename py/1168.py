import sys
input = lambda: sys.stdin.readline().strip()

def init(node, nl, nr):
    if nl == nr:
        tree[node] = 1
        return tree[node]
    
    mid = nl + nr >> 1
    tree[node] = init(node * 2, nl, mid) + init(node * 2 + 1, mid + 1, nr)
    return tree[node]

def update(node, nl, nr, k):
    if nl == nr:
        tree[node] -= 1
        return nl
    
    mid = nl + nr >> 1
    if tree[node * 2] >= k:
        ret = update(node * 2, nl, mid, k)

    else:
        ret = update(node * 2 + 1, mid + 1, nr, k - tree[node * 2])
    
    tree[node] = tree[node * 2] + tree[node * 2 + 1]
    return ret

n, k = map(int, input().split())
tree = [0] * 4 * n
init(1, 0, n - 1)

rev = 1
ans = []
for sz in range(n, 0, -1):
    rev += k - 1
    rev %= sz
    if rev == 0:
        rev = sz

    ans.append(str(update(1, 0, n - 1, rev) + 1))

print(f'<{", ".join(ans)}>')
