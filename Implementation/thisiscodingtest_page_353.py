import sys
from collections import deque

def cal_bfs(col, row, visited):
    value = 0
    union = deque()
    temp = list()
    temp.append((col, row))
    union.append((col, row))
    visited[col][row] = True
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    count = 1
    while union:
        x, y = union.popleft()
        value += arr[x][y]
        for i in range(4):
            t_x, t_y = x+dx[i], y+dy[i]
            if 0 <= t_x < n and 0 <= t_y < n and not visited[t_x][t_y] and l <= abs(arr[x][y] - arr[t_x][t_y]) <= r:
                union.append((t_x, t_y))
                temp.append((t_x, t_y))
                count += 1
                visited[t_x][t_y] = True

    if count > 1:
        for i in temp:
            arr[i[0]][i[1]] = value//count

    return count


n, l, r = map(int, sys.stdin.readline().split())
arr = list()
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

result = 0
while 1:
    evidence = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                temp = cal_bfs(i, j, visited)
                if temp > 1:
                    evidence = True
    if not evidence:
        break
    else:
        result += 1

print(result)