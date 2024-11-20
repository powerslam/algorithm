import sys
from functools import cmp_to_key
input = lambda: sys.stdin.readline().strip()

n = int(input())
digits = [[] for _ in range(10)]

offset = ord('0')
for num in input().split():
    digits[ord(num[0]) - offset].append(num)

def cmp(x, y):
    if x + y > y + x:
        return -1
    
    elif x + y < y + x:
        return 1
    
    return 0

res = ''
for digit in digits[::-1]:
    if not digit: continue
    digit = sorted(digit, key=cmp_to_key(cmp))
    res += ''.join(map(str, digit))

print(res if res[0] != '0' else 0)
