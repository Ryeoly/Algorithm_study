import sys
import heapq

n = int(sys.stdin.readline())
pos = []
nag = []
zero = 0
result = 0

for i in range(n):
    number = int(sys.stdin.readline())
    if number == 0:
        zero += 1
    elif number == 1:
        result += 1
    elif number < 0:
        heapq.heappush(nag, number)
    elif number > 0:
        heapq.heappush(pos, -number)

for i in range(int(len(pos)//2)):
    first = heapq.heappop(pos)
    second = heapq.heappop(pos)
    result += first*second

if pos:
    result -= heapq.heappop(pos)

for i in range(int(len(nag)//2)):
    first = heapq.heappop(nag)
    second = heapq.heappop(nag)
    result += first*second

if nag and zero == 0:
    result += heapq.heappop(nag)

print(result)
