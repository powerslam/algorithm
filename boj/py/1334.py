n = input()
half = n[:len(n) // 2 + (len(n) % 2 != 0)]

def isPalin(n):
    l = len(n) // 2
    for i in range(l):
        if n[i] != n[len(n) - i - 1]:
            return False
    return True

tmp = half + half[:len(n) // 2][::-1]
if n == '9':
    print(11)

elif isPalin(tmp) and int(tmp) > int(n):
    print(half + half[:len(n) // 2][::-1])

else:
    half = str(int(half) + 1)
    half += half[:len(n) // 2][::-1]
    print(half)