import sys
input = lambda: sys.stdin.readline().strip()

m, k = int(input()), 0
for _ in range(m):
    o, x = input().split(), 0
    if len(o) == 2:
        x = int(o[1])
    o = o[0]
    
    if o == 'add': k |= 1 << x
    elif o == 'remove': k &= ~(1 << x)
    elif o == 'check': print(int(k & (1 << x) == (1 << x)))
    elif o == 'toggle': k ^= (1 << x)
    elif o == 'all': k = (1 << 21) - 1
    elif o == 'empty': k = 0