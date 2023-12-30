import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
mat = [0] * n
rel = [set() for _ in range(n)]

for i in range(n):
    ln = input()
    for j, c in enumerate(ln):
        # 친구 관계면 집합에 추가하기
        if c == 'Y':
            rel[i].add(j)

cnt = 0
for i in range(n):
    tot = rel[i].copy()
    for fri in rel[i]:
        tot |= rel[fri]
    
    if cnt < len(tot):
        cnt = len(tot) - 1

print(cnt)
