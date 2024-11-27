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

t = input()
p = input()

pi = compute_pi(p)
# print(pi)
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

print(len(ans))
print(*ans)

# [0, 0, 0, 0, 1, 2, 0]