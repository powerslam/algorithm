import sys
input = lambda: sys.stdin.readline().strip()
mod = 1000

# 경로 압축 시 값을 증가시켜 줘야 함
def solve(n):
    root = list(range(n + 1))
    cost = [0] * (n + 1)

    # leaf 노드가 아니라면 경로 압축 시 값을 더해야 함
    def find(p):
        if p == root[p]: return 0, p

        _cost, _root = find(root[p])
        if root[p] != root[root[p]]:
            cost[p] += _cost
        
        root[p] = _root
        return cost[p], root[p]

    def union(p, q):
        _, pp = find(p)
        _, pq = find(q)

        if pp == pq: return
        cost[p] += abs(q - p) % mod
        root[p] = q

    while True:
        o, *v = input().split()
        if o == 'O': break

        if o == 'E':
            find(int(v[0]))
            print(cost[int(v[0])])

        else:
            i, j = int(v[0]), int(v[1])
            union(i, j)

for _ in range(int(input())):
    n = int(input())
    solve(n)
