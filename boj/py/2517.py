import sys
input = lambda: sys.stdin.readline().strip()

def merge_sort(arr):
    if len(arr) == 1:
        return
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            arr[k] = left[i]
            i += 1
            k += 1

        else:
            cnt[right[j][1]] += len(left) - i
            arr[k] = right[j]
            j += 1
            k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

n = int(input())
arr = [(int(input()), i) for i in range(n)]
cnt = [0] * n
merge_sort(arr)
for v in cnt:
    print(v + 1)
