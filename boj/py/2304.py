import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
info = sorted([list(map(int, input().split())) for _ in range(n)])
stack = [tuple(info[0])]
mH, ans = stack[-1][1], 0 # 일단 높이만

for x, h in info[1:]:
    while stack:
        if stack[-1][1] == mH or stack[-1][1] > h:
            break
        
        rev = stack.pop()
        if stack[-1][1] > rev[1]:
            ans -= rev[1] * (rev[0] - stack[-1][0])
            ans -= (stack[-1][1] - rev[1])

        else:
            ans -= stack[-1][1] * (rev[0] - stack[-1][0])
    
    # 추가될 높이가 더 적은 경우
    if stack[-1][1] > h:
        ans += h * (x - stack[-1][0])
        ans += (stack[-1][1] - h)

    else:
        ans += stack[-1][1] * (x - stack[-1][0])
        mH = max(mH, h)

    #print(ans)
    stack.append((x, h))

print(ans + stack[-1][1])
