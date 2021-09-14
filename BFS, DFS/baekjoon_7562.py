import sys
from collections import deque


def search(x, y, _x, _y, l):
    queue = deque()
    queue.append((x, y))
    dy, dx = (1, -1, -2, -2, -1, 1, 2, 2), (2, 2, 1, -1, -2, -2, -1, 1)

    while queue:
        cur_x, cur_y = queue.popleft()
        if cur_x == _x and cur_y == _y:
            queue.clear()
            return arr[cur_x][cur_y]
        for i in range(8):
            n_x, n_y = cur_x +dx[i], cur_y + dy[i]
            if l > n_x >= 0 and l > n_y >= 0:
                if arr[n_x][n_y] == 0:
                    arr[n_x][n_y] = arr[cur_x][cur_y] + 1
                    queue.append((n_x,n_y))


if __name__ == "__main__":
    n = int(sys.stdin.readline())

    for i in range(n):
        l = int(sys.stdin.readline())
        arr = [[0 for j in range(l)] for q in range(l)]
        x, y = map(int, sys.stdin.readline().split())
        _x, _y = map(int, sys.stdin.readline().split())
        print(search(x, y, _x, _y, l))
