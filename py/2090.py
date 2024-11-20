n = int(input())
nums = list(map(int, input().split()))
M = max(nums)

gcd = lambda a, b: a if b == 0 else gcd(b, a % b)

total1 = 1
for num in nums:
    total1 *= num

total2 = 0
for num in nums:
    total2 += (total1 // num)

g = gcd(total1, total2)
print(total1//g, total2//g, sep='/')