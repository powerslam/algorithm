import sys

input = lambda: sys.stdin.readline().strip()

r, c = map(int, input().split())

word = []
words = []
for i in range(r):
    tmp, s = '', input()
    words += [s]
    
    for t in s:
        if t == '#':
            if len(tmp) > 1:
                word.append(tmp)
            tmp = ''
        
        else: tmp += t

    if tmp and len(tmp) > 1:
        word.append(tmp)

for i in range(c):
    tmp = ''
    for j in range(r):
        t = words[j][i]
        if t == '#':
            if len(tmp) > 1:
                word.append(tmp)
            tmp = ''

        else: tmp += t

    if tmp and len(tmp) > 1:
        word.append(tmp)

print(sorted(word)[0])
