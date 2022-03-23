import sys
from collections import deque


def bfs(arr, x, y):
    que = deque()
    que.append((x, y))
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [1, -1, 0, 1, -1, 0, 1, -1, 0]

    while que:
        _x, _y = que.popleft()
        for i in range(9):
            t_x , t_y = dx[i] + _x, dy[i] + _y
            if 0 <= t_x < h and 0 <= t_y < w and arr[t_x][t_y] == 1:
                que.append((t_x, t_y))
                arr[t_x][t_y] = -1


while 1:
    w, h = map(int, sys.stdin.readline().split())
    answer = 0
    if w == 0 and h == 0:
        break

    arr = list()
    for i in range(h):
        arr.append(list(map(int, sys.stdin.readline().split())))

    for i in range(w):
        for j in range(h):
            if arr[j][i] == 1:
                bfs(arr, j, i)
                answer += 1

    print(answer)