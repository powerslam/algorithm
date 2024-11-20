import sys
from functools import cmp_to_key
input = lambda: sys.stdin.readline().strip()

def cmp(v, w):
    if v[1] * w[0] != v[0] * w[1]:
        return v[1] * w[0] < v[0] * w[1]
    
    if v[1] != w[1]:
        return v[1] > w[1]
    
    return v[0] < w[0]

def ccw(a, b, c):
    r = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return 1 if r < 0 else -1 if r > 0 else 0

def convex(pt):
    st, visited = [0, 1, 2], [False] * n
    visited[1] = True
    visited[2] = True

    start_ccw = ccw(pt[0], pt[1], pt[2])

    for i in range(3, len(pt)):
        bcd = ccw(pt[st[-2]], pt[st[-1]], pt[i])

        if start_ccw == 0 or start_ccw == bcd:
            start_ccw = bcd
            visited[i] = True
            st.append(i)
        
        else:
            while len(st) > 1:
                bcd = ccw(pt[st[-2]], pt[st[-1]], pt[i])
                if bcd == 0 or start_ccw == bcd:
                    break

                else: 
                    visited[st[-1]] = False
                    st.pop()

            visited[i] = True
            st.append(i)

    for i in range(st[-1] - 1, -1, -1):
        if visited[i]: continue

        bcd = ccw(pt[st[-2]], pt[st[-1]], pt[i])

        if start_ccw == 0 or start_ccw == bcd:
            start_ccw = bcd
            visited[i] = True
            st.append(i)
        
        else:
            while len(st) > 1:
                bcd = ccw(pt[st[-2]], pt[st[-1]], pt[i])
                if bcd == 0 or start_ccw == bcd:
                    break

                else: 
                    visited[st[-1]] = False
                    st.pop()

            visited[i] = True
            st.append(i)

    return start_ccw, st

tc = int(input())
for _ in range(tc):
    n = int(input())
    
    m = n // 5
    if m * 5 < n: m += 1

    pt = []
    for _ in range(m):
        li = list(map(int, input().split()))
        for i in range(0, len(li), 2):
            pt.append((li[i], li[i + 1]))

    pt.sort(key=lambda x: (-x[1], x[0]))

    start_ccw, hull = convex(pt)

    if start_ccw == -1:
        hull = hull[::-1]

    ans1 = len(hull) - 1
    ans2 = [pt[0]]

    for i in range(1, len(hull) - 1):
        if ccw(pt[hull[i - 1]], pt[hull[i]], pt[hull[i + 1]]) == 0:
            ans1 -= 1
            continue

        ans2.append(pt[hull[i]])

    if ans1 == 1:
        ans2.append(pt[hull[-2]])

    print(ans1)
    for x, y in ans2:
        print(x, y)

