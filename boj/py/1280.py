import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
tree = [[0, 0] for _ in range(800008)]

def update(node, nl, nr, k, v):
    if nr < k or k < nl:
        return
    
    tree[node][0] += v
    tree[node][1] += 1

    if nl == nr:
        return
    
    mid = (nl + nr) // 2
    update(node * 2, nl, mid, k, v)
    update(node * 2 + 1, mid + 1, nr, k, v)

def query(node, nl, nr, sl, sr):
    if nr < sl or sr < nl:
        return [0, 0]
    
    if sl <= nl and nr <= sr:
        return tree[node]
    
    mid = (nl + nr) // 2
    left = query(node * 2, nl, mid, sl, sr)
    right = query(node * 2 + 1, mid + 1, nr, sl, sr)

    return [left[0] + right[0], left[1] + right[1]]

ans, mod = 1, 1000000007
poss = [int(input()) + 1 for _ in range(n)]
update(1, 1, 200000, poss[0], poss[0])
for pos in poss[1:]:
    update(1, 1, 200000, pos, pos)
    small = query(1, 1, 200000, 1, pos - 1)
    large = query(1, 1, 200000, pos + 1, 200000)

    cost = small[1] * pos - small[0]
    cost += large[0] - large[1] * pos

    ans = (ans * cost) % mod

print(ans)
