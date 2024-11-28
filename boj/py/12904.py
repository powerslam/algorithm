from collections import deque

s, t = input(), input()
q = deque(list(t))
direction = True

while len(s) != len(q):
    if direction:
        last = q.pop()

    else:
        last = q.popleft()

    if last == 'B':
        direction = not direction

q = list(q)
if not direction:
    q = q[::-1]

print(int(s == ''.join(q)))
