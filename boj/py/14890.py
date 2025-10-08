import sys
input = lambda: sys.stdin.readline().strip()

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

def solve():
    for i in range(n):
        j = 0
        while j < n - 1:
            diff = board[i][j + 1] - board[i][j]
            if abs(diff) > 1:
                visited[i][:] = [999] * n
                break

            elif abs(diff) == 1:
                scope = board[i][j + 1:j + l + 1] if diff < 0 else board[i][j - l + 1:j + 1]
                start = (j + 1) if diff < 0 else (j - l + 1)
                
                flag = start < 0 or len(scope) != l
                if flag:
                    visited[i][:] = [999] * n
                    break
                
                for k in range(len(scope)):
                    if scope[k] != scope[0]:
                        flag = True

                    visited[i][start + k] += 1

                if flag:
                    visited[i][:] = [999] * n
                    break

            j += 1

    ret = 0
    for i in range(n):
        flag = True
        for j in range(n):
            flag = flag and (visited[i][j] < 2)

        ret += int(flag)

    return ret

ans = solve()
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i):
        if i == j: continue

        board[i][j], board[j][i] = board[j][i], board[i][j]

ans += solve()
print(ans)
