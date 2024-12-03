# 2252 문제 기반

import sys
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())

ans = []
indegree = [0] * (n + 1)
adj = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    # 인접 리스트 만들 때 진입차수 덧셈
    indegree[b] += 1

# 진입차수가 0인 정점 탐색하기
st = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        st.append(i)

# stack에서 하나씩 빼면서 탐색하기
ans = []
while st:
    v = st.pop()
    # 방문 시마다 정답에 추가하기
    ans.append(v)

    for nxt in adj[v]:
        # 자식 정점 방문 시 진입 차수 -= 1
        indegree[nxt] -= 1

        # 만약에 자식 정점의 진입 차수가 0이라면
        if indegree[nxt] == 0:
            # stack에 추가하기
            st.append(nxt)

# 정답 출력하기
print(*ans)
