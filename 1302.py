import sys
input = lambda: sys.stdin.readline().strip()

ans = dict()
for book in [input() for _ in range(int(input()))]:
    if book in ans: ans[book] -= 1
    else: ans[book] = -1

print(sorted(ans.items(), key=lambda x: (x[1], x[0]))[0][0])