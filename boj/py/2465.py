import sys
input = lambda: sys.stdin.readline().strip()

def init(node, nl, nr):
    if nl == nr:
        tree[node] = 1
        return tree[node]
    
    mid = nl + nr >> 1
    tree[node] = init(node * 2, nl, mid) + init(node * 2 + 1, mid + 1, nr)
    return tree[node]

def query(node, nl, nr, v):
    if nl == nr:
        tree[node] = 0
        return nl

    mid = nl + nr >> 1
    if tree[node * 2] >= v:
        ret = query(node * 2, nl, mid, v)

    else:
        ret = query(node * 2 + 1, mid + 1, nr, v - tree[node * 2])
    
    tree[node] = tree[node * 2] + tree[node * 2 + 1]
    return ret

n = int(input())
nums = sorted([int(input()) for _ in range(n)])
order = list(map(int, input().split()))

tree = [0] * 4 * (n + 100)
init(1, 0, n - 1)
ans = [0] * n

for i in range(n - 1, -1, -1):
    idx = query(1, 0, n - 1, order[i] + 1)
    ans[i] = nums[idx]
    
print(*ans, sep='\n')
