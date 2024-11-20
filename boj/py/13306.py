import sys
import io

sys.setrecursionlimit(2 * 10 ** 5 + 10)

n, q = 200000, 199999

# output 리스트가 입력 역할을 하도록 설정
output = []  # 이전 코드의 결과 리스트로 채우세요
output.append("200000 199999")
# output 리스트에 나머지 데이터를 추가...

for i in range(2, n + 1):
    output.append(str(i - 1))

for i in range(q):
    output.append(f"1 {i + 2} 1")

for i in range(n - 1):
    output.append(f"0 {i + 2}")

# output 리스트를 입력처럼 사용할 수 있도록 설정
sys.stdin = io.StringIO("\n".join(output))

input = lambda: sys.stdin.readline().strip()

n, q = map(int, input().split())
root = list(range(n + 1))
_root = list(range(n + 1))

def find(p):
    if p == root[p]:
        return p
    
    root[p] = find(root[p])
    return root[p]

def union(p, q):
    p = find(p)
    q = find(q)

    root[p] = q

for i in range(n - 1):
    _root[i + 2] = int(input())
    
order = []
for _ in range(n + q - 1):
    o, *v = map(int, input().split())
    if o == 0:
        order.append([o, v[0], _root[v[0]]])
    
    else:
        order.append([o, v[0], v[1]])

ans = []
for o, v0, v1 in order[::-1]:
    if o == 0:
        union(v0, v1)

    else:
        ans.append('YES' if find(v0) == find(v1) else 'NO')

for a in ans[::-1]:
    print(a)
