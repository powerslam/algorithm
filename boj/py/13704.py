import sys
input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())
sn = int(n ** 0.5)
arr = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    arr[i] ^= arr[i - 1]

m = int(input())
quries = [list(map(int, input().split())) + [i] for i in range(m)]
quries.sort(key=lambda x: (x[0] // sn, x[1]))

ans = 0
anss = [0] * m
cnt = [0] * (1 << 21)
l = quries[0][0] - 1
r = l - 1
for i in range(m):
    ll, rl = quries[i][0] - 1, quries[i][1]

    while r < rl:
        r += 1
        ans += cnt[k ^ arr[r]]
        cnt[arr[r]] += 1

    while r > rl:
        cnt[arr[r]] -= 1
        ans -= cnt[k ^ arr[r]]
        r -= 1

    while l < ll:
        cnt[arr[l]] -= 1
        ans -= cnt[k ^ arr[l]]
        l += 1

    while l > ll:
        l -= 1
        ans += cnt[k ^ arr[l]]
        cnt[arr[l]] += 1

    anss[quries[i][2]] = ans

print(*anss, sep='\n')
