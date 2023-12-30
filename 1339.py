import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
count = dict()


for _ in range(n):
    a = input()

    digit = 1
    for c in a[::-1]:
        if c not in count: count[c] = 0
        count[c] += digit
        digit *= 10

ans = 0
count = sorted([count[k] for k in count])[::-1]
for i, v in enumerate(count):
    ans += v * (9 - i)

print(ans)
