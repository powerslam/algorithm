import sys
input = lambda: sys.stdin.readline().strip()

l = int(input())
p = input()

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

pi = compute_pi(p)
print(l - pi[-1])
