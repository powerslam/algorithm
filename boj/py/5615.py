import sys
input = lambda: sys.stdin.readline().strip()

primes = [2, 7, 61]

def power(n, k, mod):
    ret = 1
    while k > 0:
        if k % 2 == 1:
            ret = ret * n % mod

        k //= 2
        n = n * n % mod

    return ret

def miller_rabin(n, a):
    k, r = n - 1, 0

    while k % 2 == 0:
        k //= 2
        r += 1

    # k 가 홀수 인 경우에는 1, n - 1 일 때 소수
    d = power(a, k, n)
    if d == 1 or d == n - 1:
        return True
    
    # k 가 짝수인 경우에는 n - 1 만 소수
    for _ in range(r - 1):
        d = power(d, 2, n)
        if d == n - 1:
            return True

    return False

def is_prime(n):
    if n in primes: return True
    if n == 1 or n % 2 == 0: return False

    for prime in primes:
        if not miller_rabin(n, prime):
            return False
    
    return True

ans, n = 0, int(input())
for i in range(n):
    num = 2 * int(input()) + 1

    if is_prime(num):
        ans += 1

print(ans)
