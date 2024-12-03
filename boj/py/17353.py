import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))

tree = [0] * 4 * n
lazy = [[0, 0] for _ in range(4 * n)]

def init(node, nl, nr):
	if nl == nr:
		tree[node] = arr[nl]
		return
	
	mid = nl + nr >> 1
	init(node * 2, nl, mid)
	init(node * 2 + 1, mid + 1, nr)
	tree[node] = tree[node * 2] + tree[node * 2 + 1]

init(1, 0, n - 1)

def update_lazy(node, nl, nr):
	if lazy[node][0] != 0:
		s, e = lazy[node]
		total = (s + e) * (nr - nl + 1) // 2
		tree[node] += total
		
		if nl != nr:
			mid = nr - nl + 2 >> 1
			diff = (e - s) // (nr - nl)
			
			lazy[node * 2][0] += s
			lazy[node * 2][1] += s + diff * (mid - 1)
			
			lazy[node * 2 + 1][0] += s + diff * (mid - 0)
			lazy[node * 2 + 1][1] += e
			
		lazy[node][0] = lazy[node][1] = 0

def update_range(node, nl, nr, sl, sr):
	update_lazy(node, nl, nr)
	
	if sr < nl or nr < sl:
		return
	
	if sl <= nl and nr <= sr:
		lazy[node][0] += nl - sl + 1
		lazy[node][1] += nr - sl + 1
		update_lazy(node, nl, nr)
		return
	
	mid = nl + nr >> 1
	update_range(node * 2, nl, mid, sl, sr)
	update_range(node * 2 + 1, mid + 1, nr, sl, sr)
	tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(node, nl, nr, idx):
	update_lazy(node, nl, nr)
	
	if idx < nl or nr < idx:
		return 0
	
	if nl == nr:
		return tree[node]
		
	mid = nl + nr >> 1
	return query(node * 2, nl, mid, idx) + query(node * 2 + 1, mid + 1, nr, idx)

q = int(input())
for _ in range(q):
	o, *param = map(int, input().split())
	if o == 1:
		l, r = param
		update_range(1, 0, n - 1, l - 1, r - 1)
			
	else:
		x = param[0]
		print(query(1, 0, n - 1, x - 1))
