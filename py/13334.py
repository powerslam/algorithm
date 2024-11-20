import sys
input = lambda: sys.stdin.readline().strip()

from bisect import bisect_right as upper_bound

arr = []
m = int(1e9)
n = int(input())
t = [list(map(int, input().split())) for _ in range(n)]
ans, d = 0, int(input())

for h, o in t:
    if h > o: h, o = o, h

    if o - h > d: continue

    m = min(m, h)
    arr.append([h, 1, 0])
    arr.append([o, 0, 1])

arr.append([m, 0, 0])
arr.sort()

start_sum = [0] * len(arr)
end_sum = [0] * len(arr)

for i in range(1, len(arr)):
    start_sum[i] = start_sum[i - 1] + arr[i][1]
    end_sum[i] = end_sum[i - 1] + arr[i][2]

# for i in range(len(arr)):
#     print(arr[i][0], end=' ')
# print()    

# for i in range(len(arr)):
#     print(arr[i][1], end=' ')
# print()

# for i in range(len(arr)):
#     print(arr[i][2], end=' ')
# print()

# print(end_sum[128], start_sum[49])

# arr[0][1] = arr[1][1]
# arr[0][2] = arr[1][2]

for i in range(1, len(arr)):
    if arr[i][1] == 0: continue
    
    right = upper_bound(arr, arr[i][0] + d, key=lambda x: x[0]) - 1
    res = end_sum[right] - start_sum[i - 1]
    ans = max(ans, res)

    # print(arr[i][0], arr[right][0])
    # print(right, end_sum[right], i - 1, start_sum[i - 1])

print(ans)
