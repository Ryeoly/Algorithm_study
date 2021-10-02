import sys
from collections import deque


def bfs(n, m, arr):
    queue = deque()
    queue.append((0, 0, 0))
    dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
    one_floor = [[0 for _ in range(m)] for _ in range(n)]
    two_floor = [[0 for _ in range(m)] for _ in range(n)]
    one_floor[0][0] = 1
    two_floor[0][0] = 1
    while queue:
        x, y, check= queue.popleft()
        if x == n - 1 and y == m - 1:
            queue.clear()
            if check == 1:
                return two_floor[n-1][m-1]
            else:
                return one_floor[n-1][m-1]

        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m and arr[next_x][next_y] == 0:
                if check == 1 and two_floor[next_x][next_y] == 0:
                    queue.append((next_x, next_y, check))
                    two_floor[next_x][next_y] = two_floor[x][y] + 1
                elif check == 0 and one_floor[next_x][next_y] == 0:
                    queue.append((next_x, next_y, check))
                    one_floor[next_x][next_y] = one_floor[x][y] + 1

            elif 0 <= next_x < n and 0 <= next_y < m and check == 0 and arr[next_x][next_y] == 1:
                queue.append((next_x, next_y, 1))
                two_floor[next_x][next_y] = one_floor[x][y] + 1

        if len(queue) == 0:
            return -1


n, m = map(int, sys.stdin.readline().split())
arr = list()

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))

print(bfs(n, m, arr))

# 다시 생각해보고 다시 스스로 짜보자, 시간 복잡도 생각해보고, 효율적으로 바꾸어 보자