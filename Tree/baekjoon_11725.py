import sys
from collections import deque

def find_child(arr, n):
    que = deque([1])
    result = [-1] * (n+1)
    while que:
        cur = que.popleft()
        for i in arr[cur]:
            if result[i] == -1 and i != 1:
                result[i] = cur
                que.append(i)

    for i in range(2, n+1):
        print(result[i])

    return

n = int(sys.stdin.readline())
arr = dict()
for i in range(1, n+1):
    arr[i] = []

for i in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

find_child(arr, n)


