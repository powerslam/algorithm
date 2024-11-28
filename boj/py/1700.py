import sys
input = lambda: sys.stdin.readline().strip()

inf = 9876543210
n, k = map(int, input().split())
seqs = list(map(int, input().split()))
last = [-1] * (k + 1)
future = [-1] * (k + 1)

for i in range(k):
    if last[seqs[i]] != -1:
        future[last[seqs[i]]] = i - last[seqs[i]]

    last[seqs[i]] = i
    future[i] = inf

ans, size = 0, 0
used = [-1] * (k + 1)
# print(future)

for i in range(k):
    rev_idx = 1
    for j in range(1, k + 1):
        used[j] -= 1
        if used[j] > used[rev_idx]:
            rev_idx = j

    if used[seqs[i]] > -1:
        used[seqs[i]] = future[i]
        continue

    elif size == n:
        used[rev_idx] = -1
        ans += 1
        size -= 1

    used[seqs[i]] = future[i]
    size += 1

print(ans)
