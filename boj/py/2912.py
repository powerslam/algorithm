import sys
# sys.stdin = open('patuljci.in.2', 'r')
input = lambda: sys.stdin.readline().strip()

n, c = map(int, input().split())
sn = int(n ** 0.5)
color = list(map(int, input().split()))
max_c = max(color)

m = int(input())
queries = [list(map(lambda x: int(x) - 1, input().split())) + [i] for i in range(m)]
queries.sort(key=lambda x: (x[0] // sn, x[1]))

cnt = [0] * 300001
ans = [0] * m

_ans = 0
interval = (queries[0][1] - queries[0][0] + 1) // 2
for i in range(queries[0][0], queries[0][1] + 1):
    # print(len(color), i)
    cnt[color[i]] += 1
    if cnt[color[i]] > interval:
        _ans = color[i]

ans[queries[0][2]] = _ans
for i in range(1, m):
    prev_s, prev_e, _ = queries[i - 1]
    now_s, now_e, ans_idx = queries[i]
    interval = (now_e - now_s + 1) // 2

    if cnt[_ans] <= interval:
        _ans = 0

    idx = prev_s
    while idx < now_s:
        cnt[color[idx]] -= 1
        idx += 1

    idx = prev_s - 1
    while idx >= now_s:
        cnt[color[idx]] += 1
        idx -= 1

    idx = prev_e + 1
    while idx <= now_e:
        cnt[color[idx]] += 1
        idx += 1

    idx = prev_e
    while idx > now_e:
        cnt[color[idx]] -= 1
        idx -= 1

    for j in range(1, max_c + 1):
        if cnt[j] > interval:
            ans[ans_idx] = j
            break

print(*map(lambda x: 'no' if x == 0 else f'yes {x}', ans), sep='\n')
