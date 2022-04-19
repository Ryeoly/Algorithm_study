import sys
from collections import deque

# old version
# def find_1(arr, m, n):
#     pos = deque()
#     for i in range(m):
#         for j in range(n):
#             if arr[j][i] == 1:
#                 pos.append((j, i))
#     return pos
#
#
# def result(arr, m, n):
#     maximum = 0
#     for i in range(m):
#         for j in range(n):
#             if arr[j][i] == 0:
#                 return -1
#             if arr[j][i] > maximum:
#                 maximum = arr[j][i]
#     return maximum-1
#
#
# def bfs(arr, m, n, queue):
#     dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             n_x, n_y = x+dx[i], y+dy[i]
#             if 0 <= n_x < n and 0 <= n_y < m and arr[n_x][n_y] == 0:
#                 arr[n_x][n_y] = arr[x][y] + 1
#                 queue.append((n_x,n_y))
#     return arr
#
#
# m, n = map(int, sys.stdin.readline().split())
# arr = list()
# for i in range(n):
#     arr.append(list(map(int, sys.stdin.readline().split())))
#
# queue = find_1(arr, m, n)
# if len(queue) == m*n:
#     print(0)
#
# print(result(bfs(arr, m, n, queue), m, n))

# code review
m, n = map(int, sys.stdin.readline().split())
arr = list()
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

que = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            que.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while que:
    col, row = que.popleft()

    for i in range(4):
        n_col, n_row = col+dx[i], row+dy[i]
        if 0 <= n_col < n and 0 <= n_row < m and arr[n_col][n_row] == 0:
            arr[n_col][n_row] = arr[col][row] + 1
            que.append((n_col, n_row))

result = -2
check = True
for i in range(n):
    for j in range(m):
        if arr[i][j] > result:
            result = arr[i][j]
        if arr[i][j] == 0:
            check = False

if not check:
    print(-1)
elif result <= 1:
    print(0)
else:
    print(result-1)