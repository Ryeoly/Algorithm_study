import sys

def clean(arr):
    global r
    global c
    global d
    for i in range(4):
        temp_x = r + dx[(d-i+4)%4]
        temp_y = c + dy[(d-i+4)%4]

        if 0 <= temp_x < n and 0 <= temp_y < m:
            if arr[temp_x][temp_y] == 0:
                d = (d-i+3) % 4
                r = temp_x
                c = temp_y
                return True
    return False


n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
arr = list()
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
back_x = [1, 0, -1, 0]
back_y = [0, -1, 0, 1]
result = 0

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

while 1:
    if arr[r][c] == 0:
        arr[r][c] = 2
        result += 1

    evidence = clean(arr)
    if not evidence:
        t_x = r + back_x[d]
        t_y = c + back_y[d]
        if 0 <= t_x < n and 0 <= t_y < m and arr[t_x][t_y] != 1:
                r = t_x
                c = t_y
                continue
        else:
            break

print(result)