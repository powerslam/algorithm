import sys
input = lambda: sys.stdin.readline().strip()

class Snake:
    def __init__(self, map_size):
        self.direction = 0
        self.dy = [0, 1, 0, -1]
        self.dx = [1, 0, -1, 0]

        self.now = (map_size, map_size)
        self.boundary = 2 * map_size + 1

        # 형식은 (x1, y1, x2, y2)
        # 초기 값 : 경계선
        self.lines = [
            (self.boundary, 0, self.boundary, self.boundary - 1, -5),
            (0, self.boundary, self.boundary - 1, self.boundary, -4),
            (-1, 0, -1, self.boundary - 1, -3),
            (0, -1, self.boundary - 1, -1, -2),
            (int(1e9), int(1e9), int(1e9), int(1e9), -1)
        ]

    def move(self, m, cnt) -> bool:
        # print(self.now)

        x1, y1 = self.now
        x2, y2 = x1 + m * self.dx[self.direction], y1 + m * self.dy[self.direction]
        
        ret = int(1e9)
        for x3, y3, x4, y4, _cnt in self.lines:
            if _cnt + 1 == cnt: continue

            abc = self.ccw([x1, y1], [x2, y2], [x3, y3])
            abd = self.ccw([x1, y1], [x2, y2], [x4, y4])
            cda = self.ccw([x3, y3], [x4, y4], [x1, y1])
            cdb = self.ccw([x3, y3], [x4, y4], [x2, y2])

            # 아래 두 케이스의 경우 겹치는 것임. 시간 잘 계산해서 반환
            # 넷 중 한 성분이 일직선인 경우
            if abc * abd == 0 and cda * cdb == 0:
                if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4):                     
                    if y1 == y2:
                        if x1 < x2: ret = min(ret, abs(x3 - x1))
                        else: ret = min(ret, abs(x1 - x4))
                    
                    else:
                        if y1 < y2: ret = min(ret, abs(y3 - y1))
                        else: ret = min(ret, abs(y1 - y4))

            # 교차? 하는 경우
            elif abc * abd <= 0 and cda * cdb <= 0:
                if y3 == y4: ret = min(ret, abs(y3 - y1))
                else: ret = min(ret, abs(x3 - x1))

        self.lines.append((x1, y1, x2, y2, cnt))
        # self.lines.sort()
        self.now = (x2, y2)

        if ret == int(1e9):
            return True, 0

        return False, ret

    def roataion(self, dir):
        self.direction += (1 if dir == 'R' else 3)
        self.direction %= 4

    def ccw(self, a, b, c):
        r = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        return 1 if r < 0 else -1 if r > 0 else 0

l = int(input())
n = int(input())
query = [input().split() for _ in range(n)]
query.append([int(1e9), 'L'])

ans, cnt = 0, 0
snake = Snake(l)
for a, b in query:
    # print(snake.now, '\n', snake.lines)

    a = int(a)
    safe, pos = snake.move(a, cnt)
    
    if not safe:
        # 일단 죽었다고 출력
        # print('die, pos : ', pos)
        ans += pos
        break

    else:
        ans += a

    snake.roataion(b)
    cnt += 1
    # print('dir', snake.direction)

print(ans)
