import sys
input = lambda: sys.stdin.readline().strip()

MOD = 10000

def mul(a, b):
    return [
        [(a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD, 
         (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD],
    
        [(a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD, 
         (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD]   
    ]

def my_pow(a, b): # pow(list, int)
    if b == 1: 
        return a
    
    n = my_pow(a, b // 2)
    tmp = mul(n, n)
    
#    print('tmp :', tmp)
    
    return tmp if b % 2 == 0 else mul(a, tmp)

while True:
    n = int(input())
    if n == -1:
        break

    if n == 0:
        print(0)

    elif n < 3:
        print(1)

    else:
        print(sum(my_pow([[1, 1], [1, 0]], n - 2)[0]) % MOD)
