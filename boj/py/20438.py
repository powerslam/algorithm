import sys
input = lambda: sys.stdin.readline().strip()

n, k, q, m = map(int, input().split())

sleep = set(map(int, input().split()))
code = set(map(int, input().split()))
code = code - sleep

arr = [0] * (n + 3)
for c in code:
    for i in range(c, n + 3, c):
        if i not in sleep:
            arr[i] = 1

cum = [0] * (n + 3)
for i in range(1, n + 3):
    cum[i] = cum[i - 1] + arr[i]

print(arr, cum)
for _ in range(m):
    a, b = map(int, input().split())
    print(cum[b] - cum[a - 1])
