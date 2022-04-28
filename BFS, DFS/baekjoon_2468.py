import sys
from collections import deque
from copy import deepcopy

def bfs(arr, number, n, col, row):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    que = deque()
    que.append((col, row))
    arr[col][row] = number

    while que:
        x, y = que.popleft()
        for i in range(4):
            t_x = x + dx[i]
            t_y = y + dy[i]
            if 0 <= t_x < n and 0 <= t_y < n and arr[t_x][t_y] > number:
                que.append((t_x, t_y))
                arr[t_x][t_y] = number
    return arr

def execut(arr, number, n):
    temp_arr = deepcopy(arr)
    count = 0
    for i in range(n):
        for j in range(n):
            if temp_arr[i][j] > number:
                temp_arr = bfs(temp_arr, number, n, i, j)
                count += 1
    return count

n = int(sys.stdin.readline())
arr = list()
result = list()
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

min_value = 101
max_value = 0
for i in range(n):
    t_max = max(arr[i])
    t_min = min(arr[i])
    if t_max > max_value:
        max_value = t_max
    if t_min < min_value:
        min_value = t_min

for i in range(min_value):
    result.append(1)
for number in range(min_value, max_value):
    result.append(execut(arr, number, n))

print(max(result))

