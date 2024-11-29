import sys
input = lambda: sys.stdin.readline().strip()

n, t = map(int, input().split())
sn = int(n ** 0.5)
arr = list(map(int, input().split()))
queries = [list(map(lambda x: int(x) - 1, input().split())) + [i] for i in range(t)]
queries.sort(key=lambda x: (x[0] // sn, x[1]))
ans = [0] * t
cnt = [0] * (int(1e6) + 1)

_ans = 0
for i in range(queries[0][0], queries[0][1] + 1):
    _ans += arr[i] * (2 * cnt[arr[i]] + 1)
    cnt[arr[i]] += 1

ans[queries[0][2]] = _ans

for i in range(1, t):
    prev_s, prev_e, _ = queries[i - 1]
    now_s, now_e, ans_idx = queries[i]

    idx = prev_s - 1
    while idx >= now_s:
        _ans += arr[idx] * (2 * cnt[arr[idx]] + 1)
        cnt[arr[idx]] += 1
        idx -= 1
        
    idx = prev_s
    while idx < now_s:
        _ans -= arr[idx] * (2 * cnt[arr[idx]] - 1)
        cnt[arr[idx]] -= 1
        idx += 1

    idx = prev_e
    while idx > now_e:
        _ans -= arr[idx] * (2 * cnt[arr[idx]] - 1)
        cnt[arr[idx]] -= 1
        idx -= 1

    idx = prev_e + 1
    while idx <= now_e:
        _ans += arr[idx] * (2 * cnt[arr[idx]] + 1)
        cnt[arr[idx]] += 1
        idx += 1

    ans[ans_idx] = _ans

print(*ans, sep='\n')
