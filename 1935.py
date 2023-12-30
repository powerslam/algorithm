import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
expr = input()

ans = 0
stack = []
number = dict()
for ex in expr:
    if ex.isalpha():
        if ex not in number:
            number[ex] = int(input())

        stack += [number[ex]]
    
    else:
        term = stack[-1]
        stack.pop()  
        if ex == '+':
            stack[-1] += term
        
        elif ex == '-':
            stack[-1] -= term
    
        elif ex == '*':
            stack[-1] *= term
        
        elif ex == '/':
            stack[-1] /= term

print('%.2f' % (stack[-1]))
