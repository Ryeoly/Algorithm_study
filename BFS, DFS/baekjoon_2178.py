import sys
from collections import deque


def bfs(arr, n, m):
    queue = deque()
    queue.append((0,0))
    dx, dy = (0, 0 , 1, -1), (1, -1, 0, 0)

    while queue:
        x, y = queue.popleft()

        #오히려 밑에 3줄은 매번 검사하므로, 모든 루트를 search 하고 arr[n-1][m-1]을
        #return하는 방향이 좋을 수 있겠다.
        if x == n-1 and y == m-1:
            queue.clear()
            return arr[x][y]

        for i in range(4):
            if 0 <= x+dx[i] < n and 0 <= y+dy[i] < m and arr[x+dx[i]][y+dy[i]] == 1:
                queue.append((x+dx[i], y+dy[i]))
                arr[x+dx[i]][y+dy[i]] = arr[x][y] + 1


n, m = map(int, sys.stdin.readline().split())
arr = list()
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))
print(bfs(arr, n, m))