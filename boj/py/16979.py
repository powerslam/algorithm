import sys
input = lambda: sys.stdin.readline().strip()

maxN = 1 << 17
n, m = map(int, input().split())
_nums = list(enumerate(map(int, input().split())))
nums = [0] * n

sn, idx = int(n ** 0.5), 0
compress = dict()
for i, num in sorted(_nums, key=lambda x: x[1]):
    if num not in compress:
        compress[num] = idx
        idx += 1

    nums[i] = compress[num]

queries = [list(map(lambda x: int(x) - 1, input().split())) + [i] for i in range(m)]
queries.sort(key=lambda x: (x[0] // sn, x[1]))

tree = [0] * maxN * 2

def update(k, v):
    k += maxN - 1

    while k > 1:
        tree[k] += v
        k >>= 1

def query(sl, sr):
    sl += maxN - 1
    sr += maxN - 1

    ret = 0
    while sl <= sr:
        if sl % 2 == 1:
            ret += tree[sl]
            sl += 1
        
        if sr % 2 == 0:
            ret += tree[sr]
            sr -= 1

        sl >>= 1
        sr >>= 1
    
    return ret

cnt = 0
ans = [0] * m
idx = queries[0][0]
while idx <= queries[0][1]:
    update(nums[idx], 1)
    cnt += query(nums[idx] + 1, 99999)
    idx += 1

ans[queries[0][2]] = cnt

for i in range(1, m):
    prev_s, prev_e, _ = queries[i - 1]
    now_s, now_e, ans_idx = queries[i]

    idx = prev_s
    while idx < now_s:
        cnt -= query(0, nums[idx] - 1)
        update(nums[idx], -1)
        idx += 1

    idx = prev_s - 1
    while idx >= now_s:
        cnt += query(0, nums[idx] - 1)
        update(nums[idx], 1)
        idx -= 1

    idx = prev_e + 1
    while idx <= now_e:
        cnt += query(nums[idx] + 1, 99999)
        update(nums[idx], 1)
        idx += 1
    
    idx = prev_e
    while idx > now_e:
        cnt -= query(nums[idx] + 1, 99999)
        update(nums[idx], -1)
        idx -= 1

    ans[ans_idx] = cnt

print(*ans, sep='\n')
