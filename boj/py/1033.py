import sys
input = lambda: sys.stdin.readline().strip()

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    
    return a

n = int(input())
info = []
root, rank = [0] * n, [1] * n
cost = [[[0, 0] for _ in range(n)] for _ in range(n)]
ans = [1] * n

def find(p):
    if root[p] == p: return p
    fp = find(p)

    p1, q1 = cost[root[p]][p]
    p2, q2 = cost[fp][root[p]]
    
    np, nq = p1 * p2, q1 * q2
    g = gcd(np, nq) 

    np //= g
    nq //= g

    cost[fp][p] = [np, nq]

    return root[p]

def union(p, q):
    fp = find(p)
    fq = find(q)

    if fp == fq:
        return
    
    # 크기가 더 큰 집합에 붙이기
    if rank[p] < rank[q]:
        root[q] = p
        rank[p] += rank[q]

    else:
        rank[p] = q
        rank[q] += rank[p]

for _ in range(n - 1):
    a, b, p, q = map(int, input().split())

    g = gcd(p, q)

    p //= g
    q //= g

    cost[a][b][0] = p
    cost[a][b][1] = q
    
    cost[b][a][0] = q
    cost[b][a][1] = p

    union(a, b)

# 한 번씩 순회해서 path 압축하기
for p in range(n):
    fp = find(p)
    a, b = cost[fp][p]
    ans[fp] *= 
