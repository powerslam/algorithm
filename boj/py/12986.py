import sys
input = lambda: sys.stdin.readline().strip()

n, q = map(int, input().split())
sn = int(n ** 0.5)
nums = [0] + list(map(lambda x: int(x) + int(1e5), input().split()))

quries, ans = [], [0] * q
for i in range(q):
    a, b = map(int, input().split())
    quries.append((a, b, i))

quries.sort(key=lambda x: (x[0] // sn, x[1]))

_ans = 0
cnt = [0] * (int(2e5) + 1)
cntcnt = [0] * (int(2e5) + 1)
for i in range(quries[0][0], quries[0][1] + 1):
    cntcnt[cnt[nums[i]]] -= 1
    cnt[nums[i]] += 1
    _ans = max(_ans, cnt[nums[i]])
    cntcnt[cnt[nums[i]]] += 1

ans[quries[0][2]] = _ans

for i in range(1, q):
    prev_s, prev_e, _ = quries[i - 1]
    now_s, now_e, ans_idx = quries[i]

    idx = prev_s
    while idx < now_s:
        if cntcnt[cnt[nums[idx]]] - 1 == 0 and cnt[nums[idx]] == _ans:
            _ans -= 1

        cntcnt[cnt[nums[idx]]] -= 1
        cnt[nums[idx]] -= 1
        cntcnt[cnt[nums[idx]]] += 1
        idx += 1

    idx = prev_s - 1    
    while idx >= now_s:
        cntcnt[cnt[nums[idx]]] -= 1
        cnt[nums[idx]] += 1
        _ans = max(_ans, cnt[nums[idx]])
        cntcnt[cnt[nums[idx]]] += 1
        idx -= 1

    idx = prev_e + 1
    while idx <= now_e:
        cntcnt[cnt[nums[idx]]] -= 1
        cnt[nums[idx]] += 1
        _ans = max(_ans, cnt[nums[idx]])
        cntcnt[cnt[nums[idx]]] += 1
        idx += 1
    
    idx = prev_e
    while idx > now_e:
        if cntcnt[cnt[nums[idx]]] - 1 == 0 and cnt[nums[idx]] == _ans:
            _ans -= 1

        cntcnt[cnt[nums[idx]]] -= 1
        cnt[nums[idx]] -= 1
        cntcnt[cnt[nums[idx]]] += 1
        idx -= 1

    ans[ans_idx] = _ans

print(*ans, sep='\n')
