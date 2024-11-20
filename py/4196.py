import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
tree = [0] * (n * 4)
lazy = [0] * (n * 4)


def init(node, start, end):
    if start == end:
        tree[node] = nums[start]

    else:
        mid = (start + end) // 2
        tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)

    return tree[node]


def update_lazy(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0


def update_range(node, start, end, left, right, diff):
    update_lazy(node, start, end)
    if(left > end or right < start):
        return

    if(left <= start and end <= right):
        tree[node] += (end - start + 1) * diff
        if start != end:
            lazy[node * 2] += diff
            lazy[node * 2 + 1] += diff
        return

    mid = (start + end) // 2
    update_range(node * 2, start, mid, left, right, diff)
    update_range(node * 2 + 1, mid + 1, end, left, right, diff)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def sum(node, start, end, left, right):
    update_lazy(node, start, end)

    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return sum(node * 2, start, mid, left, right) + sum(node * 2 + 1, mid + 1, end, left, right)

m = int(input())

init(1, 0, n - 1)
for _ in range(m):
    line = list(map(int, input().split()))

    if line[0] == 1:
        b, c, d = line[1:]
        update_range(1, 0, n - 1, b - 1, c - 1, d)

    else:
        b = line[1]
        print(sum(1, 0, n - 1, b - 1, b - 1))
