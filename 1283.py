import sys
input = lambda: sys.stdin.readline().strip()

chk = [False] * 27

n = int(input())
for words in [input().split() for _ in range(n)]:
    for idx, word in enumerate(words):
        if not chk[ord(word[0].lower()) - ord('a')]:
            chk[ord(word[0].lower()) - ord('a')] = True
            words[idx] = '[' + word[0] + ']' + word[1:]
            print(' '.join(words))
            break
    else:
        flag = False
        for i, word in enumerate(words):
            if flag: break
            for j, c in enumerate(word):
                if not chk[ord(c.lower()) - ord('a')]:
                    chk[ord(c.lower()) - ord('a')] = True
                    words[i] = word[:j] + '[' + word[j] + ']' + word[j + 1:]
                    print(' '.join(words))
                    flag = True
                    break
        
        else: 
            if not flag: print(' '.join(words))