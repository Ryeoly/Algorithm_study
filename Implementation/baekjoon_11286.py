import heapq
import sys

n = int(sys.stdin.readline())
plus = list()
minus = list()
for i in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(plus, x)
    elif x < 0:
        heapq.heappush(minus, x*-1)
    else:
        if len(plus) == 0 and len(minus) == 0:
            print(0)
        elif len(plus) == 0 and len(minus) != 0:
            print(heapq.heappop(minus)*-1)
        elif len(plus) != 0 and len(minus) == 0:
            print(heapq.heappop(plus))
        elif plus[0] < minus[0]:
            print(heapq.heappop(plus))
        elif plus[0] >= minus[0]:
            print(heapq.heappop(minus)*-1)