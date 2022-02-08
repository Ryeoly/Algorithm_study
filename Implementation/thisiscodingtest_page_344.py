import sys
def bfs(arr, virus):
    new_virus = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in virus:
        number, col, row = i[0], i[1], i[2]

        for q in range(4):
            n_c, n_r = col + dx[q], row + dy[q]
            if 0 <= n_c < n and 0 <= n_r < n and arr[n_c][n_r] == 0:
                arr[n_c][n_r] = number
                new_virus.append((number, n_c, n_r))


    return arr, new_virus


n, k = map(int, sys.stdin.readline().split())
arr = list()
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            virus.append((arr[i][j], i, j))
virus.sort()
s, x, y = map(int, sys.stdin.readline().split())

sec = 0

while sec < s:
    sec += 1
    arr, virus = bfs(arr, virus)

print(arr[x - 1][y - 1])
