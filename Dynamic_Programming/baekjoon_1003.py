import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    arr = list()
    arr.append((1, 0))
    arr.append((0, 1))
    if n == 0:
        print(arr[0][0], arr[0][1])
    elif n == 1:
        print(arr[1][0], arr[1][1])
    else:
        for j in range(2, n+1):
            arr.append((arr[j-1][0] + arr[j-2][0], arr[j-1][1] + arr[j-2][1]))
        print(arr[n][0], arr[n][1])