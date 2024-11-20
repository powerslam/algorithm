n = int(input())
for num in map(int, input().split()):
    print(int(num == int(num ** 0.5) ** 2), end=' ')