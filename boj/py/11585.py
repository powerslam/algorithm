import sys
input = lambda: sys.stdin.readline().strip()

def compute_pi(p):
    m = len(p)
    pi = [0] * (m + 1)
    i, j = 1, 0

    while i < m:
        if p[i] == p[j]:
            i += 1
            j += 1
            pi[i] = j

        elif j == 0:
            i += 1
            pi[i] = j

        else:
            j = pi[j]

    return pi

nn = int(input())
t = input().replace(' ', '')
t *= 2
t = t[:-1]

p = input().replace(' ', '')

pi = compute_pi(p)
n, m = len(t), len(p)

ans = []
i, j = 0, 0
while i < n:
    if t[i] == p[j]:
        i += 1
        j += 1

        if j == m:
            ans.append(i - j + 1)
            j = pi[j]
    
    elif j == 0:
        i += 1

    else:
        j = pi[j]

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

g = gcd(len(ans), nn)
print(len(ans) // g, '/', nn // g, sep='')
