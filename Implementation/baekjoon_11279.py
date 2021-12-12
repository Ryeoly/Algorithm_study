import heapq
import sys

n = int(sys.stdin.readline())
arr = list()
for i in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(arr, -1*x)
    else:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)*-1)