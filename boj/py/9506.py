import sys
input = lambda: sys.stdin.readline().strip()

while True:
    n = int(input())
    if n == -1: break
    li = [i for i in range(1, n) if n % i == 0]
    if n == sum(li): print(n, '=', ' + '.join(map(str, li)))
    else: print(f'{n} is NOT perfect.')
