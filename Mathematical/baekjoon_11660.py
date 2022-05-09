import sys
n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
value = []
for i in range(n):
    temp = [arr[i][0]]
    for j in range(1, n):
        temp.append(temp[j-1] + arr[i][j])
    value.append(temp)


for i in range(m):
    result = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for p in range(x2-x1+1):
        if y1 > 1:
            result += (value[p + x1 - 1][y2-1] - value[p + x1 - 1][y1-2])
        else:
            result += (value[p + x1 - 1][y2 - 1])
    print(result)