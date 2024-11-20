import sys
input = lambda: sys.stdin.readline().strip()

def find(p):
    if root[p] == p:
        return p
    
    root[p] = find(root[p])
    return root[p]

def union(p, q):
    p, q = find(p), find(q)

    if p == q: return
    root[p] = q

n = int(input())
q = int(input())
mod = int(1e9) + 7

fibo = [0, 1, 1, 2]
for _ in range(4, int(1e6) + 1):
    fibo.append((fibo[-1] + fibo[-2]) % mod)

root = list(range(n + 1))

ans = [0] * (n + 1)

# 마지막 쿼리부터 이걸 적용하면 괜찮긴 한데
queries = [list(map(int, input().split())) for _ in range(q)][::-1]
for l, r in queries:
    i = l
    while i <= r:
        pi = find(i)
        if pi == i and ans[i] == 0:
            ans[i] = fibo[i - l + 1]
            union(i, r)
            i += 1

        else:
            i = pi + 1

for num in ans[1:]:
    print(num, end=' ')
