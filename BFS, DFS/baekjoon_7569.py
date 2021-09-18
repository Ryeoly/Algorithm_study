import sys
from collections import deque


def find_1(arr, m, n, h):
    pos = deque()
    for i in range(m):
        for j in range(n*h):
            if arr[j][i] == 1:
                pos.append((j, i))
    return pos


def result(arr, m, n, h):
    maximum = 0
    for i in range(m):
        for j in range(n*h):
            if arr[j][i] == 0:
                return -1
            if arr[j][i] > maximum:
                maximum = arr[j][i]
    return maximum-1


def bfs(arr, m, n, queue, h):
    dx, dy = (0, 0, 1, -1, n, -1*n), (1, -1, 0, 0, 0, 0)
    _dx, _dy = (0, 0, 1, n, -1 * n), (1, -1, 0, 0, 0)  # n의 배수
    dx_, dy_ = (0, 0, -1, n, -1 * n), (1, -1, 0, 0, 0) # n-1의 배수
    while queue:
        x, y = queue.popleft()

        if x%n == 0:
            for i in range(5):
                n_x, n_y = x+_dx[i], y+_dy[i]
                if 0 <= n_x < n*h and 0 <= n_y < m and arr[n_x][n_y] == 0:
                    arr[n_x][n_y] = arr[x][y] + 1
                    queue.append((n_x,n_y))
        elif (x+1)%n == 0:
            for i in range(5):
                n_x, n_y = x+dx_[i], y+dy_[i]
                if 0 <= n_x < n*h and 0 <= n_y < m and arr[n_x][n_y] == 0:
                    arr[n_x][n_y] = arr[x][y] + 1
                    queue.append((n_x,n_y))
        else:
            for i in range(6):
                n_x, n_y = x+dx[i], y+dy[i]
                if 0 <= n_x < n*h and 0 <= n_y < m and arr[n_x][n_y] == 0:
                    arr[n_x][n_y] = arr[x][y] + 1
                    queue.append((n_x,n_y))
    return arr


m, n, h = map(int, sys.stdin.readline().split())
arr = list()
for i in range(n*h):
    arr.append(list(map(int, sys.stdin.readline().split())))

queue = find_1(arr, m, n, h)
if len(queue) == m*n:
    print(0)

print(result(bfs(arr, m, n, queue, h), m, n, h))

# 7576번의 코드를 활용하기 위해 높이가 있는 3차원 배열을 2차원 배열로 저장 후 이용하다 보니,
# bfs 함수에서 높이 처리에 미숙했다. 높이간 간섭하면 안되는 n의 배수, n-1의 배수가
# 다른 층의 과일에 간섭하는 일이 생겼다. 2차원 배열이 아닌 3차원 배열로 구현한다면
# 보다 쉽고 간단하게 구현 가능할 것 같다.
