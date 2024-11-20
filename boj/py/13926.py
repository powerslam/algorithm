import sys
input = lambda: sys.stdin.readline().strip()

import random

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

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

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

def pollard_rho(n):
    if is_prime(n):
        return n
    
    if n == 1:
        return 1
    
    if n % 2 == 0:
        return 2

    if n == 1: return n

    x = random.randint(2, n)
    y = x
    c = random.randint(1, n)
    d = 1

    while d == 1:
        x = (x * x % n + c + n) % n
        y = (y * y % n + c + n) % n
        y = (y * y % n + c + n) % n
        d = gcd(abs(x - y), n)

        if d == n:
            return pollard_rho(n)
    
    if is_prime(d):
        return d
    
    return pollard_rho(d)

factors = []
n = int(input())
ans = n
while n > 1:
    p = pollard_rho(n)
    if n % p == 0:
        ans //= p
        ans *= (p - 1)

    while n % p == 0: 
        n //= p

if n != 1:
    ans /= n
    ans *= (n - 1)

print(ans)
