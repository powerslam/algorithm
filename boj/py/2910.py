n, c = map(int, input().split())
arr = list(map(int, input().split()))

tmp = dict()
for i, num in enumerate(arr):
    if num not in tmp:
        tmp[num] = [0, i]

    tmp[num][0] += 1

arr = list(tmp.items())
arr.sort(key=lambda x: (-x[1][0], x[1][1]))

for v, c in arr:
    print(f'{v} ' * c[0], end='')
