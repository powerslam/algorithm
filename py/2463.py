import sys
input = lambda: sys.stdin.readline().strip()

def find(p):
    if p == root[p]:
        return p
    
    root[p] = find(root[p])
    return root[p]

def union(p, q):
    p, q = find(p), find(q)

    if p == q:
        ret = 0
        
    elif size[p] < size[q]:
        root[p] = q
        ret = size[q] * size[p]
        size[q] += size[p]

    else:
        root[q] = p
        ret = size[p] * size[q]
        size[p] += size[q]

    return ret

n, m = map(int, input().split())
root = list(range(n + 1))
size = [1] * (n + 1)

edges, cum = [], [0] * m
for _ in range(m):
    x, y, w = map(int, input().split())

    if y < x:
        x, y = y, x

    edges.append((w, x, y))

edges.sort()
cum[0] = edges[0][0]
for i in range(1, m):
    cum[i] = cum[i - 1] + edges[i][0]

edges.reverse()
cum.reverse()

ans = 0
# print(cum)
for (w, x, y), acc in zip(edges, cum):
    ret = union(x, y)
    ans += ret * acc
    # print(ans, ret, acc, x, y, w)

print(ans % int(1e9))
