import sys
input = lambda: sys.stdin.readline().rstrip()

from heapq import heappush as push, heappop as pop

n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]

# 정점별 가장 짧은 가중치 구하기
shortest_weight = [min(adj[i], key=lambda x: x if x > 0 else int(1e7)) for i in range(n)]

# 가장 짧은 가중치의 합 == 외판원 순회 로직의 하한
shortest_edge_sum = sum(shortest_weight)

# A*
# (하한, 방문 정점, 방문 여부(bitmask))
# 하한 = 가장 짧은 out-edge의 합 + cost 이므로
# 시작할 때에는 시작 정점을 제외한 나머지 정점들의 가장 짧은 out-edge의 합을 하한으로 잡고 시작함
q = [(shortest_edge_sum - shortest_weight[0], 0, 1)]

# q가 빌 때까지
while q:
    # (하한, 현재 정점, 방문 여부)
    bound, v, visited = pop(q)

    # 만약에 모든 정점에 방문했다면
    if visited == (1 << n) - 1:
        print(bound, adj[u][0], u)
        break

    # 정점 v에 대해서
    for u in range(n):
        # 만약에 가중치가 0이라면 간선이 없는 거니까 pass
        if adj[v][u] == 0:
            continue

        # 전에 방문했던 정점이어도 pass
        if visited & (1 << u):
            continue

        # (bound : u를 선택했기 때문에 bound 값에서 u의 하한을 뺌. 동시에 v -> u 로 가는 가중치를 더해줌
        #  v : 다음 방문 정점인 u를 넣음
        #  visited : u를 방문했기 때문에 visited에 u를 추가함)
        
        # 이번 정점이 마지막 정점이라면 -> 리프 노드라는 뜻
        if (visited | (1 << u)) == (1 << n) - 1:
            print((bound + adj[v][u] - shortest_weight[u] + adj[u][0], u, visited | (1 << u)))
        #     # 마지막 정점에서 0으로 가는 간선이 없다면 pass
        #     if adj[u][0] == 0:
        #         continue
            
        #     # 경우에 따라 복귀 간선의 값이 너무 커서 최적해가 아닌 경우가 존재함
        #     # 따라서 끝내지 않고 큐에 넣음
        #     push(q, (bound + adj[v][u] - shortest_weight[u] + adj[u][0], u, visited | (1 << u)))

        # else:
        push(q, (bound + adj[v][u] - shortest_weight[u], u, visited | (1 << u)))
