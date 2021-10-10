import sys

n = int(sys.stdin.readline())
arr = list()
for i in range(n):
    line = list(map(str, sys.stdin.readline().split()))
    if line[0] == "push":
        arr.append(line[1])
    elif line[0] == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr)-1])
    elif line[0] == "size":
        print(len(arr))
    elif line[0] == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr)-1])
            arr.pop()
    elif line[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    else:
        print("error")