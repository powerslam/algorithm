import sys
input = lambda: sys.stdin.readline().strip().split()

a, b = map(int, input())
q, r = divmod(a, b)
if r < 0:
    q += 1
    r = a - b * q

print(q)
print(r)