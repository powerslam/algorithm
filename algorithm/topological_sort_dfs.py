# 2252 문제 기반

import sys
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())

ans = []
visited = [False] * (n + 1)
adj = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)

def dfs(v):
    # 일반적인 dfs
    if visited[v]:
        return

    visited[v] = True
    for nxt in adj[v]:
        if visited[nxt]:
            continue

        dfs(nxt)
    
    # 후위 순회 방식이기 때문에 모든 자식 정점 탐색이 종료된 후
    # ans 배열에 추가됨
    ans.append(v)

# 정점 1번이 항상 root가 아니기 때문에
# 모든 정점에 대해 dfs를 수행해야 함
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)

# dfs 결과의 역순이 정답이기 때문에 [::-1] 로 출력
print(*ans[::-1])
