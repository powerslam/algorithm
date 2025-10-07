import sys
input = lambda: sys.stdin.readline().strip()

scope = {
    1: [(0, 1)],
    2: [(0, -1), (0, 1)],
    3: [(-1, 0), (0, 1)],
    4: [(0, -1), (-1, 0), (0, 1)],
    5: [(0, -1), (-1, 0), (0, 1), (1, 0)]
}

nxt_dir = {
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1)
}

n, m = map(int, input().split())
LIMIT = n * m
board = []

cam_pos = []
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for j in range(m):
        if 0 < board[i][j] < 6:
            cam_pos.append((i, j))

def mark_board(pos, dirs, v):
    for dy, dx in dirs:
        y, x = pos[0] + dy, pos[1] + dx
        while 0 <= y < n and 0 <= x < m and board[y][x] <= 5:
            if board[y][x] <= 0:
                board[y][x] += v
            
            y += dy
            x += dx

def calc_board():
    ret = 0
    for i in range(n):
        for j in range(m):
            ret += int(board[i][j] == 0)

    return ret

def solve(idx):
    ret = LIMIT
    y, x = cam_pos[idx]
    for _ in range(4):
        mark_board(cam_pos[idx], scope[board[y][x]], -1)
        if idx + 1 < len(cam_pos):
            ret = min(ret, solve(idx + 1))

        else:
            ret = min(ret, calc_board())

        mark_board(cam_pos[idx], scope[board[y][x]], 1)
        for i in range(len(scope[board[y][x]])):
            scope[board[y][x]][i] = nxt_dir[scope[board[y][x]][i]]

    return ret

print(solve(0) if cam_pos else calc_board())
