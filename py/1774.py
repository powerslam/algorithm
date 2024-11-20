import sys
input = lambda: sys.stdin.readline().strip()
dist = lambda x, y: (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

def find(p):
    if p == root[p]:
        return p

    root[p] = find(root[p])
    return root[p]

def union(p, q):
    p = find(p)
    q = find(q)

    if p == q: return
    root[p] = q

pts = []
n, m = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    pts.append((x, y))

arr = []
for i in range(n):
    for j in range(n):
        arr.append((dist(pts[i], pts[j]), i + 1, j + 1))
arr.sort()

ans = 0
root = list(range(n + 1))

for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)

for d, i, j in arr:
    if find(i) == find(j): continue
    
    ans += d ** 0.5
    union(i, j)

print('%.2f' % ans)

