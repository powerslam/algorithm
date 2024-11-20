import sys
sys.setrecursionlimit(int(1e6))
input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())
adj = [[] for _ in range(n)]

for _ in range(n - 1):
    p, c = map(int, input().split())
    adj[p].append(c)

apple = list(map(int, input().split()))

dp = [0] * n

def back_tracking(v, depth):
    global dp
    dp[v] = apple[v]

    if depth == k: return dp[v]
    
    for nxt in adj[v]:
        dp[v] += back_tracking(nxt, depth + 1)

    return dp[v]

back_tracking(0, 0)
print(dp[0])
