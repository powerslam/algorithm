import sys
input = lambda: sys.stdin.readline().strip()

from heapq import heappop as pop, heappush as push

n = int(input())
arr = list(map(int, input().split()))
node, ordered = tuple(arr), tuple(sorted(arr))

m = int(input())
modifys = [list(map(int, input().split())) for _ in range(m)]

cost = {node: 0}
q = [(0, node)]
while q:
    _cost, now = pop(q)
    if now == ordered:
        print(_cost)
        break

    for a, b, c in modifys:
        tmp = list(now)
        tmp[a - 1], tmp[b - 1] = tmp[b - 1], tmp[a - 1]
        nxt = tuple(tmp)

        if nxt in cost and cost[nxt] <= cost[now] + c:
            continue

        cost[nxt] = cost[now] + c
        push(q, (cost[nxt], nxt))

else:
    print(-1)
