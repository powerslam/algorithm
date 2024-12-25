import sys
input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())
sn = int(n ** 0.5)
sz = 100000

nums = list(map(int, input().split()))
tree = [0] * (sz + 1)

def update(k, v):
    while k <= sz:
        tree[k] += v
        k += k & -k

def query(k):
    ret = 0
    while k > 0:
        ret += tree[k]
        k -= k & -k
    return ret

def range_query(nl, nr):
    if nl < 1:
        nl = 1

    if nr > sz:
        nr = sz
    
    return query(nr) - query(nl - 1)
    
m = int(input())
queries = [list(map(lambda x: int(x) - 1, input().split())) + [i] for i in range(m)]
queries.sort(key=lambda x: (x[0] // sn, x[1]))

cnt = 0
ans = [0] * m
idx = queries[0][0]
while idx <= queries[0][1]:
    cnt += range_query(nums[idx] - k, nums[idx] + k)
    update(nums[idx], 1)
    idx += 1

ans[queries[0][2]] = cnt

for i in range(1, m):
    prev_s, prev_e, _ = queries[i - 1]
    now_s, now_e, ans_idx = queries[i]

    idx = prev_s
    while idx < now_s:
        update(nums[idx], -1)
        cnt -= range_query(nums[idx] - k, nums[idx] + k)
        idx += 1

    idx = prev_s - 1
    while idx >= now_s:
        cnt += range_query(nums[idx] - k, nums[idx] + k)
        update(nums[idx], 1)
        idx -= 1

    idx = prev_e + 1
    while idx <= now_e:
        cnt += range_query(nums[idx] - k, nums[idx] + k)
        update(nums[idx], 1)
        idx += 1
    
    idx = prev_e
    while idx > now_e:
        update(nums[idx], -1)
        cnt -= range_query(nums[idx] - k, nums[idx] + k)
        idx -= 1

    ans[ans_idx] = cnt

print(*ans, sep='\n')
