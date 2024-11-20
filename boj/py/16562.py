import sys
input = lambda: sys.stdin.readline().strip()

n, m, k = map(int, input().split())
root = list(range(n + 1))

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

cost = [0] + list(map(int, input().split()))
for _ in range(m):
    v, w = map(int, input().split())
    union(v, w)

for i in range(1, n + 1):
    find(i)
    cost[root[i]] = min(cost[root[i]], cost[i])

ans = 0
for i in range(1, n + 1):
    if i == find(i):
        ans += cost[i]

print(ans if ans <= k else 'Oh no')
