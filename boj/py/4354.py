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

while True:
    p = input()
    if p == '.':
        break

    pi = compute_pi(p)
    pattern = len(p) - pi[-1]

    if len(p) % pattern == 0:
        print(len(p) // pattern)

    else:
        print(1)
