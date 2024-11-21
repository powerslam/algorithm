import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
sn = int(n ** 0.5)
arr = [0] + list(map(int, input().split()))
m = int(input())

ans = [0] * m
dcnt, cnt = 0, [0] * (int(1e6) + 1)
quries = [list(map(int, input().split())) + [i] for i in range(m)]
quries.sort(key=lambda x: (x[0] // sn, x[1]))

idx = quries[0][0]
while idx <= quries[0][1]:
    if cnt[arr[idx]] == 0:
        dcnt += 1
    
    cnt[arr[idx]] += 1
    idx += 1

ans[quries[0][2]] = dcnt

for i in range(1, m):
    prev_s, prev_e, _ = quries[i - 1]
    now_s, now_e, ans_idx = quries[i]

    idx = prev_s
    while idx < now_s:
        cnt[arr[idx]] -= 1
        if cnt[arr[idx]] == 0:
            dcnt -= 1

        idx += 1

    idx = prev_s - 1
    while idx >= now_s:
        if cnt[arr[idx]] == 0:
            dcnt += 1
        
        cnt[arr[idx]] += 1
        idx -= 1

    idx = prev_e + 1
    while idx <= now_e:
        if cnt[arr[idx]] == 0:
            dcnt += 1

        cnt[arr[idx]] += 1
        idx += 1
    
    idx = prev_e
    while idx > now_e:
        cnt[arr[idx]] -= 1
        if cnt[arr[idx]] == 0:
            dcnt -= 1

        idx -= 1

    ans[ans_idx] = dcnt

print(*ans, sep='\n')
