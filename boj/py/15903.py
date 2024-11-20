import sys
input = lambda: sys.stdin.readline().strip()

from heapq import heappush as push, heappop as pop, heapify

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapify(cards)

for _ in range(m):
    a = pop(cards)
    b = pop(cards)

    c = a + b
    push(cards, c)
    push(cards, c)

print(sum(cards))
