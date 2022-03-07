import sys
import heapq

n = int(sys.stdin.readline())
heap = []
result = 0
for i in range(n):
    heapq.heappush(heap, (int(sys.stdin.readline())))

while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    number = first + second
    result += number
    heapq.heappush(heap, number)

print(result)