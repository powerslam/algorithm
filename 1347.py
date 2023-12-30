import sys
input = lambda: sys.stdin.readline().strip()

# 남 서 북 동
dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]
dix = 0

dot, n = [0, 0], int(input())
dli = [(0, 0)]
mx, Mx, my, My = 0, 0, 0, 0
order = input()

for o in order:
    if o == 'L':
        dix = 3 if dix == 0 else (dix - 1)

    elif o == 'R':
        dix = (dix + 1) % 4
    
    elif o == 'F':
        dot[0] += dir[dix][0]
        dot[1] += dir[dix][1]

        my = min(my, dot[0])
        mx = min(mx, dot[1])

        My = max(My, dot[0])
        Mx = max(Mx, dot[1])

        dli.append((dot[0], dot[1]))

dli.sort()

My -= my
Mx -= mx

board = [['#'] * (Mx + 1) for _ in range(My + 1)]
for d in dli:
    board[d[0] - my][d[1] - mx] = '.'

for b in board:
    print(*b, sep='')
