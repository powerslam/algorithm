import sys
input = lambda: sys.stdin.readline().strip()

for _ in range(int(input())):
    idx, ans, st, pwd = 0, [], [], input()
    for c in pwd:
        if c == '<':
            if len(ans): 
                st += [ans.pop()]

        elif c == '>':
            if len(st): 
                ans += [st.pop()]

        elif c == '-':
            if len(ans):
                ans.pop()

        else:
            ans.append(c)

    ans += st[::-1]

    print(*ans, sep='')
