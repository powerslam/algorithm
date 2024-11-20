import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
size = 20
adj = [[] for _ in range(n + 1)]
info = [[-1] * size for _ in range(n + 1)]
depth = [-1] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

depth[1], stack = 0, [1]
while stack:
    root = stack.pop()
    for v in adj[root]:
        if depth[v] != -1: continue
        depth[v] = depth[root] + 1
        info[v][0] = root
        stack.append(v)

for j in range(size - 1):
    for i in range(1, n + 1):
        if info[i][j] != -1:
            info[i][j + 1] = info[ info[i][j] ][ j ]

def lca(x, y):
    if depth[x] > depth[y]: # y의 깊이가 x보다 얕으면
        x, y = y, x
    
    pow, diff = 0, depth[y] - depth[x]
    while diff:
        if diff & 1: y = info[y][pow]
        diff >>= 1
        pow += 1
    
    if x != y:
        for idx in range(size - 1, -1, -1):
            if info[y][idx] != -1 and info[y][idx] != info[x][idx]:
                y = info[y][idx]
                x = info[x][idx]

        y = info[y][0]
    return y

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
