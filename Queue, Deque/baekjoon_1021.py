from collections import deque
import math

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queue = deque(i+1 for i in range(n))
count = 0

for i in range(m):
    pos = queue.index(arr[i])
    if pos <= math.floor(len(queue)/2):
        queue.rotate(-1*pos)
        count += pos
    elif pos > math.floor(len(queue)/2):
        queue.rotate(len(queue)-pos)
        count += len(queue)-pos
    queue.popleft()

print(count)