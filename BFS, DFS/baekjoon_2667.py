import sys
from collections import deque


def find_1(arr, n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                return i, j
    return False


def bfs(arr, n):
    dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
    result = list()
    queue = deque()

    while find_1(arr, n):
        count = 0
        x, y = find_1(arr, n)
        arr[x][y] = 0
        queue.append((x, y))

        while queue:
            count += 1
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                n_x, n_y = dx[i] + cur_x, dy[i] + cur_y
                if 0 <= n_x < n and 0 <= n_y < n and arr[n_x][n_y] == 1:
                    arr[n_x][n_y] = 0
                    queue.append((n_x, n_y))
        result.append(count)

    result.sort()
    return result


n = int(sys.stdin.readline())
arr = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip()))
    arr.append(temp)

answer = bfs(arr, n)
print(len(answer))
for i in answer:
    print(i)
