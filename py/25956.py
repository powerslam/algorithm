import sys
input = lambda: sys.stdin.readline().strip()

stk = []
cnt_stk = []
n = int(input())
ans = [0 for _ in range(n + 1)]
lvl = [int(input()) for _ in range(n)]

def solve():
    for i, l in enumerate(lvl):
        if len(stk) < 2:
            stk.append((i, l))

        else:
            cnt = 0
            # 스택에 1개 이상 남았고 top 원소가 입력보다 하위 제목이면
            while len(stk) > 1 and stk[-1][1] > l:
                # top 이랑 top - 1 이 같으면
                if stk[-1][1] == stk[-2][1]:
                    # 카운트 증가
                    cnt += 1
                
                # top 이 top - 1 보다 하위 제목인 경우
                elif stk[-1][1] > stk[-2][1]:
                    # 1 차이가 아니면 return -1
                    if stk[-2][1] - stk[-1][1] != 1:
                        return -1
                    
                    else:
                        ans[stk[-2][0]] = cnt + 1
                        cnt = cnt_stk.pop()

                # top 이 top - 1 보다 상위 제목인 경우
                else: # stk[-1][1] < stk[-2][1]:
                    cnt_stk.append(cnt)
                    cnt = 0
                    continue
            
            stk.pop()

solve()
print(ans)