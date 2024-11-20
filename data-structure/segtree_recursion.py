def init(node, nl, nr):
    if nl == nr:
        segtree[node] = arr[nl]
        return segtree[node]

    mid = nl + nr >> 1
    segtree[node] = init(node * 2, nl, mid) + init(node * 2 + 1, mid + 1, nr)
    return segtree[node]

def query(node, nl, nr, sl, sr):
    # 탐색 범위에 들지 않았으므로 0을 반환
    if sr < nl or nr < sl:
        return 0
    
    # 탐색 범위에 (nl, nr)가 정확히 들어맞으므로 tree[node] 값 반환
    if sl <= nl and nr <= sr:
        return segtree[node]
    
    # 이외에는 분할 정복을 통해 값을 저장함
    mid = nl + nr >> 1
    return query(node * 2, nl, mid, sl, sr) + query(node * 2 + 1, mid + 1, nr, sl, sr)

def update_by_diff(node, nl, nr, idx, diff):
    # 업데이트 하고자 하는 인덱스가 (nl, nr) 범위에 들지 않는 경우
    # 아무것도 하지 않고 종료
    if idx < nl or nr < idx:
        return

    # diff 를 더해줌
    segtree[node] += diff

    # nl == nr 이면 leaf 노드이므로 재귀 호출 하지 않음
    # 아직 leaf 노드가 아니므로 재귀 호출
    if nl != nr:
        mid = nl + nr >> 1
        update_by_diff(node * 2, nl, mid, idx, diff)
        update_by_diff(node * 2 + 1, mid + 1, nr, idx, diff)

def update_by_value(node, nl, nr, idx, value):
    # 업데이트 하고자 하는 인덱스가 (nl, nr) 에 포함되어 있지 않다면
    # 그냥 node 값을 반환
    if idx < nl or nr < idx:
        return segtree[node]
    
    # 만약 leaf 노드라면, 값을 갱신하고 그것을 반환함.
    if nl == nr:
        segtree[node] = value
        return segtree[node]
    
    # init 과 비슷한 방식으로 업데이트 수행 
    mid = nl + nr >> 1
    segtree[node] = update_by_value(node * 2, nl, mid, idx, value) + update_by_value(node * 2 + 1, mid + 1, nr, idx, value)
    return segtree[node]

# 구간 쿼리를 적용할 배열의 크기
n = 10

# 구간 쿼리를 적용할 배열
arr = list(range(n))

# 넉넉하게 n의 4배를 segtree의 사이즈로 잡는다.
segtree = [0] * 4 * n

# segtree 초기화
# -> 문제에 따라서 초기화를 굳이 안해줘도 되는 경우 존재
init(1, 0, n - 1)
print(segtree)

print('2 ~ 5 구간의 합 :', query(1, 0, n - 1, 2, 5))

# 5번 인덱스 값을 4로 업데이트
diff = 4 - arr[5]
arr[5] = 4
update_by_diff(1, 0, n - 1, 5, diff)
print('2 ~ 5 구간의 합 (segtree) :', query(1, 0, n - 1, 2, 5))
print('2 ~ 5 구간의 합 (sum)     :', sum(arr[2:6]))

# 5번 인덱스 값을 22로 업데이트
arr[5] = 22
update_by_value(1, 0, n - 1, 5, 22)
print('2 ~ 5 구간의 합 (segtree) :', query(1, 0, n - 1, 2, 5))
print('2 ~ 5 구간의 합 (sum)     :', sum(arr[2:6]))
