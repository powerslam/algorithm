import sys
input = lambda: sys.stdin.readline().strip()

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def square(a):
    n, k, m = len(a), len(a), len(a)
    
    ret = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            for l in range(k):
                ret[i][j] += a[i][l] * a[l][j]

def power(b):
    while b != 0:
                
