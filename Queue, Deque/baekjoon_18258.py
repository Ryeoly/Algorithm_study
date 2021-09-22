from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    line = list(map(str, sys.stdin.readline().split()))
    if line[0] == "push":
        queue.append(line[1])
    elif line[0] == "pop":
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif line[0] == "size":
        print(len(queue))
    elif line[0] == "empty":
        if len(queue) != 0:
            print(0)
        else:
            print(1)
    elif line[0] == "front":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif line[0] == "back":
        if len(queue) != 0:
            print(queue[len(queue)-1])
        else:
            print(-1)
    else:
        print("error")