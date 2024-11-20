from itertools import combinations
from functools import reduce

n = int(input())
ans = n

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
use = []

for prime in primes:
    if n % prime == 0:
        ans -= n // prime
        use += [prime]

for cnt in range(2, len(use) + 1):
    for combi in combinations(use, cnt):
        ret = reduce(lambda r, c: r * c, combi, 1)
        
        ans += n // ret

print(ans)
