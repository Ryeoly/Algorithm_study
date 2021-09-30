import sys
from collections import deque
case = int(input())
for i in range(case):
    n, m = map(int, sys.stdin.readline().split())
    queue = deque(map(int, sys.stdin.readline().split()))

    number = queue[m]
    queue[m] = -1
    count = 0

    while 1:
        if queue[0] == -1 and max(queue) <= number:
            break
        if max(queue) == queue[0] and number <= max(queue):
            count += 1
            queue.popleft()
        else:
            queue.rotate(-1)

    count += 1
    print(count)