import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def merge_sort(arr):
    global cnt

    if len(arr) == 1:
        return
    
    mid = len(arr) >> 1
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        
        else:
            cnt[k] += len(left) - i
            arr[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1

tc = int(input())
for _ in range(tc):
    n = int(input())

    indicies = [0] * (n + 1)
    for i, v in enumerate(map(int, input().split())):
        indicies[v] = i

    cnt = [0] * n
    arr = [indicies[v] for v in map(int, input().split())]

    merge_sort(arr)

    print(sum(cnt))
