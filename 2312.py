import sys

input = lambda: sys.stdin.readline().strip()
lim = int(1e5)

prime, visited = [], [False] * lim
for num in range(2, lim):
    if visited[num]: continue
    prime += [num]
    
    for rev in range(num + num, lim, num):
        visited[rev] = True

for _ in range(int(input())):
    n = int(input())

    for p in prime:
        if n < p: break

        cnt = 0
        while n % p == 0:
            n //= p
            cnt += 1

        if cnt: print(p, cnt)
