import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
words = [input() for _ in range(n)]

node = set()
for i in range(len(words)):
    for j in range(len(words[i])):
        node.add(words[i][j])

adj = [[] for _ in range(26)]
indegree = [0] * 26
wrong = False
for i in range(n - 1):
    for k in range(min(len(words[i]), len(words[i + 1]))):
        if words[i][k] != words[i + 1][k]:
            adj[ord(words[i][k]) - ord('a')].append(ord(words[i + 1][k]) - ord('a'))
            indegree[ord(words[i + 1][k]) - ord('a')] += 1
            break
    else:
        if len(words[i]) > len(words[i + 1]):
            wrong = True

st = []
for nod in node:
    if indegree[ord(nod) - ord('a')] == 0:
        st.append(ord(nod) - ord('a'))

ans = []
ans_type = 0
duplicate = False
while st:
    if len(st) > 1:
        duplicate = True

    v = st.pop()
    ans.append(chr(v + ord('a')))

    for nxt in adj[v]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            st.append(nxt)

if len(ans) != len(node) or wrong:
    print('!')

elif duplicate:
    print('?')

else:
    print(*ans, sep='')
