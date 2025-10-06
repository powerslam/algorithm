import sys
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [0] * m

cumsum = [0] * n
cumsum[0] = arr[0] % m
cnt[cumsum[0]] += 1

for i in range(1, n):
    cumsum[i] = ((arr[i] % m) + (cumsum[i - 1] % m)) % m
    cnt[cumsum[i]] += 1

ans = cnt[0] + sum(map(lambda x: x * (x - 1) // 2, cnt))
print(ans)
