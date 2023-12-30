import sys
input = lambda: sys.stdin.readline().strip()

tot, ans = 0, dict()
while True:
    name = input()
    if not name: break
    if name not in ans: ans[name] = 0
    ans[name] += 1
    tot += 1

print(*sorted(['%s %.4f' % (k, v / tot * 100) for k, v in ans.items()]), sep='\n')